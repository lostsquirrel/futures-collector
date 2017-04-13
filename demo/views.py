# -*- coding:utf-8 -*-
'''
Created on 2015年5月14日

@author: zhuhua
'''
from simpletor import application

@application.RequestMapping("/")
class IndexHandler(application.RequestHandler):
    def get(self):
        self.render('index.html')