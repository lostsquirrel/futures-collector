# -*- coding:utf-8 -*-
"""
Created on 2013-3-26

@author: zhuhua
"""
import sys

import tornado.ioloop

from tornado import options

import settings
from simpletor import application

if __name__ == '__main__':
    
    port = settings.port
    if len(sys.argv) == 2:
        port = sys.argv[1]
    
    options.options.logging = "debug"
    options.parse_command_line()

    app = application.Application()
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
