# -*- coding:utf-8 -*-
from __future__ import print_function
from __future__ import print_function
import re
from evaluation.models import evaluationDataDAO as dataDAO
from simpletor.torndb import transactional

@transactional
def save_data(data):
    dataDAO.save(**data)

def get_all_data():
    data_list = dataDAO.find_all()
    for item in data_list:
        item.position_time = seconds2str(item.position_time)
    return data_list

@transactional
def remove_data(data_id):
    dataDAO.remove(data_id)

re_time_str_split = re.compile(r'[A-Za-z]')
time_str_template = ('', '%ds', '%dm%02ds', '%dh%02dm%02ds')
time_unit = ('h', 'm', 's')
def str2seconds(time_str):
    ts = [0] * 3
    for i in range(3):
        his = 0
        hie = 0
        try:
            his = time_str.index(time_unit[i - 1])
            his += 1
        except (ValueError):
            pass
        try:
            hie = time_str.index(time_unit[i])
        except (ValueError):
            pass
        if hie > 0:
            hi_ = time_str[his:hie]
            if hi_ is not None and len(hi_) > 0:
                ts[i] = int(hi_)
    total = 0

    base = 1
    for x in range(3):
        total += int(ts.pop()) * base
        base *= 60
    return total

def seconds2str(time_seconds):
    time_str = ''
    ts = [0] * 3
    index = 0
    while time_seconds > 0:
        ts[index] = (time_seconds % 60)
        time_seconds /= 60
        index += 1
    ts.reverse()

    for i in range(len(ts)):
        if ts[i] > 0:
            time_str = '%s%02d%s' % (time_str, ts[i], time_unit[i])

    if len(time_str) == 0:
        time_str = '0s'

    return time_str

if __name__ == '__main__':
    seconds = str2seconds('1h1m')
    print(seconds)
    print(seconds2str(seconds))