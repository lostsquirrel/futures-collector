# -*- coding:utf-8 -*-

from simpletor import torndb


class EvaluationData(torndb.Row):
    def __init__(self, **kwargs):
        super(EvaluationData, self).__init__(**kwargs)
        self.id = None
        self.trade_date = None
        self.position_time = -1
        self.position_time_str = ''
        self.profit = None
        self.commission = None
        self.evaluation_score = None


class EvaluationDataDAO:
    def __init__(self):
        pass

    @torndb.insert
    def save(self, **data):
        sql = '''
        INSERT INTO evaluation_data
        ( 
        trade_date, volume, profit, commission, evaluation_score 
        )
        VALUES
        (
        %(trade_date)s,  %(volume)s, %(profit)s, %(commission)s, %(evaluation_score)s
        )
        '''
        return sql

    @torndb.select
    def find_all(self):
        sql = '''
        SELECT id, trade_date, volume, profit, commission, evaluation_score
        FROM evaluation_data
        ORDER BY trade_date DESC, id DESC
        '''
        return sql

    @torndb.delete
    def remove(self, data_id):
        sql = '''
        DELETE FROM evaluation_data WHERE id = %s
        '''
        return sql


evaluationDataDAO = EvaluationDataDAO()
