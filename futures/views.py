# -*- coding:utf-8 -*-
'''
Created on 2015年5月14日

@author: zhuhua
'''
from simpletor import application

@application.RequestMapping("/data")
class DataHandler(application.RequestHandler):
    def get(self):
        self.render('k_line_data.html')

@application.RequestMapping("/item")
class ItemHandler(application.RequestHandler):
    def get(self):
        self.render('k_line_edit.html')

@application.RequestMapping("/chart")
class ChartHandler(application.RequestHandler):
    def get(self):
        self.render('k_line_chart.html')

@application.RequestMapping(r"/favicon.ico")
class IconHandler(application.RequestHandler):
    def get(self):
        self.render('favicon.ico')