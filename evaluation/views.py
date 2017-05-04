# -*- coding:utf-8 -*-

from simpletor import application

@application.RequestMapping("/evaluation/data")
class EvaluationDataHandler(application.RequestHandler):
    def get(self):
        self.render('evaluation_data.html')

@application.RequestMapping("/evaluation/stats")
class EvaluationStatsHandler(application.RequestHandler):
    def get(self):
        self.render('evaluation_stats.html')