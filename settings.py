# -*- coding:utf-8 -*-
'''
Created on 2013-3-26

@author: zhuhua
'''
import os

installed_apps = ['futures']

template_dir = os.path.join(os.path.dirname(__file__), "templates")
static_dir = os.path.join(os.path.dirname(__file__), "static")
db_user = 'futures'
db_pass = 'futures_pass'
db_name = 'futures'
db_host = '192.168.19.66'
port = 8080
