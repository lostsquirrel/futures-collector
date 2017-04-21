# -*- coding:utf-8 -*-
"""
Created on 2014年12月18日

@author: zhuhua
"""
import hashlib
import json
import random
import re
import time
from datetime import date, datetime

import application


class ValidateUtils:
    """验证工具类"""

    def __init__(self):
        pass

    @staticmethod
    def is_empty_str(string):
        if string is None or string == '':
            return True
        return False

    @staticmethod
    def is_mobile(string):
        return re.match('^1[3-8][0-9]\d{8}$', string)


validate_utils = ValidateUtils()


class JSONEncoder(json.JSONEncoder):
    """Json 编码器"""

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


def md5(source):
    """MD5"""
    _md5 = hashlib.md5()
    _md5.update(source)
    return _md5.hexdigest()


def sha1(password):
    """Password Hash"""
    _sha1 = hashlib.sha1()
    _sha1.update(password)
    return _sha1.hexdigest()


def generate_order_no():
    return '%d' % (int(time.time() * 1000 * 1000))


def generate_random(start, end):
    return int(random.Random().random() * (end - start)) + start


def str2time(date_str, pattern="%Y-%m-%d"):
    try:
        d = time.strptime(date_str, pattern)
    except ValueError:
        raise application.AppError('日期转换出错')
    return d


def str2date(date_str, pattern="%Y-%m-%d"):
    try:
        d = datetime.strptime(date_str, pattern).date()
    except ValueError:
        raise application.AppError('日期转换出错')
    return d


def str2datetime(date_str, pattern="%Y-%m-%d"):
    try:
        d = datetime.strptime(date_str, pattern)
    except ValueError:
        raise application.AppError('日期转换出错')
    return d


def get_level(score):
    grade = 0
    if score > 0:
        score_grade = (
            0, 1, 2, 4, 9, 15, 31, 58, 94, 147, 211, 286, 385, 508, 656, 829, 1026, 1307, 1644, 2037, 2486, 2991, 3608,
            4337, 5178, 6131, 7196)
        grade = len(score_grade) - 1
        while grade > 0:
            if score >= score_grade[grade]:
                break
            grade -= 1

    return grade
