# -*- coding:utf-8 -*-
"""
Created on 2013-3-26

@author: zhuhua
"""
import json

import tornado.wsgi

import settings
import utils

ApplicationBase = tornado.web.Application


class RequestMapping:
    def __init__(self, value):
        self.value = value

    def __call__(self, handler):
        self.handler = handler
        return self


def paging(page, page_size, total):
    page, page_size, total = int(page), int(page_size), int(total)
    pages = total / page_size if total % page_size == 0 else total / page_size + 1
    prev = page if page - 1 == 0 else page - 1
    _next = pages if page + 1 > pages else page + 1
    template = '''
        <ul>
            <li><a href="?page=%s">上一页</a></li>
            <li><span>第%s页</span></li>
            <li><span>共%s页</span></li>
            <li><a href="?page=%s">下一页</a></li>
        </ul>
    '''
    return template % (prev, page, pages, _next)


class RequestHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(RequestHandler, self).__init__(application, request, **kwargs)
        self.errors = dict()

    def set_current_user(self, user):
        user = json.dumps(user)
        self.set_secure_cookie('user', user)

    def get_current_user(self):
        cookie = self.get_secure_cookie('user')
        try:
            return json.loads(cookie)
        except ValueError:
            return None

    def add_error(self, error):
        if isinstance(error, AppError):
            self.errors[error.field] = error.value

    def get_error(self, field='default'):
        if field in self.errors:
            return self.errors[field]
        return ''

    def render_json(self, data):
        self.set_header('Content-Type', 'application/json;charset=UTF-8')
        self.write(json.dumps(data, cls=utils.JSONEncoder))
        self.finish()


class Security:
    """
    Security
    """

    def __init__(self, *roles):
        self.roles = roles

    def __call__(self, method):

        def __method(request, *args, **kwds):

            user = request.get_current_user()
            if user is None:
                request.redirect('/login')
                return

            if user['role'] not in self.roles:
                request.redirect('/logout')
                return
            return method(request, *args, **kwds)

        return __method


class AppError(Exception):
    """Application Logic Exception"""

    def __init__(self, message, field='default'):
        self.value = message
        self.field = field

    def __str__(self, *args, **kwargs):
        return self.value


class Application(ApplicationBase):
    def __init__(self):

        handlers = []
        installed_apps = settings.installed_apps

        for appName in installed_apps:
            app_package = __import__(appName, globals(), locals(), ['views'], -1)
            views = app_package.views

            for handlerName in dir(views):
                handler_wrapper = getattr(views, handlerName)
                if isinstance(handler_wrapper, RequestMapping):
                    handlers.append((handler_wrapper.value, handler_wrapper.handler))

        template_dir = settings.template_dir

        super(Application, self).__init__(handlers, **{
            "static_path": settings.static_dir,
            "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            "template_path": template_dir
        })
