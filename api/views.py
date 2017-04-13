# -*- coding:utf-8 -*-
from simpletor import application
from futures import services

@application.RequestMapping("/api/tags")
class Items(application.RequestHandler):
    '''获取标签列表'''

    def get(self):
        tags = services.get_items()
        self.render_json(tags)