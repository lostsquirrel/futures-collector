# -*- coding:utf-8 -*-
'''
Created on 2013-3-26

@author: zhuhua
'''
import os

installed_apps = ['futures', 'api']

template_dir = os.path.join(os.path.dirname(__file__), "templates")
static_dir = os.path.join(os.path.dirname(__file__), "static")
db_user = 'futures'
db_password = 'futures_pass'
db_name = 'futures'
# db_host = '192.168.1.139:13301'
db_host = 'mariadb_10_1_main'
pass_code = 'a'
port = 9000
