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


@application.RequestMapping("/evaluation/entry")
class EvaluationEntryHandler(application.RequestHandler):
    def get(self):
        self.render('wap_evaluation_entry.html')


@application.RequestMapping("/evaluation/history")
class EvaluationHistoryHandler(application.RequestHandler):
    def get(self):
        self.render('wap_evaluation_history.html')


@application.RequestMapping("/evaluation/total")
class EvaluationTotalHandler(application.RequestHandler):
    def get(self):
        self.render('wap_total.html')
        
@application.RequestMapping("/evaluation/analysis")
class EvaluationAnalysisHandler(application.RequestHandler):
    def get(self):
        self.render('wap_analysis.html')