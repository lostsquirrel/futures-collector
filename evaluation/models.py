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

class StatsGeneral(torndb.Row):
    def __init__(self):
        self.win_sum = 0
        self.win_max = 0
        self.win_count = 0
        self.win_volume = 0
        self.lost_sum = 0
        self.lost_min = 0
        self.lost_count = 0

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
        %(trade_date)s, %(volume)s, %(profit)s, %(commission)s, %(evaluation_score)s
        )
        '''
        return sql

    @torndb.select
    def find_all(self):
        sql = '''
        SELECT id, trade_date, position_time, volume, profit, commission, evaluation_score
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


class EvaluationStatsDAO:
    def __init__(self):
        pass

    @torndb.select
    def stats_profit_win(self):
        sql = '''
        SELECT SUM(profit) as win_sum FROM evaluation_data WHERE profit > 0
        '''
        return sql

    @torndb.get
    def stats_profit_win_unit(self, unit_dates):
        sql = '''
        SELECT SUM(profit) as win_unit FROM evaluation_data 
        WHERE profit > 0
        AND trade_date in %s
        '''
        return sql

    @torndb.select
    def stats_profit_win_max(self):
        sql = '''
        SELECT MAX(profit) as win_max FROM evaluation_data
        '''
        return sql

    @torndb.select
    def stats_profit_win_count_total(self):
        sql = '''
        SELECT COUNT(id) as win_count, SUM(volume) as win_volume FROM evaluation_data 
        WHERE profit > 0
        '''
        return sql

    @torndb.select
    def stats_profit_win_count_unit(self, unit_dates):
        sql = '''
        SELECT COUNT(id) as win_count, SUM(volume) as win_volume FROM evaluation_data 
        WHERE profit > 0
        AND trade_date in %s
        '''
        return sql

    @torndb.select
    def stats_profit_lost(self):
        sql = '''
        SELECT SUM(profit) as lost_sum FROM evaluation_data WHERE profit < 0
        '''
        return sql
    @torndb.get
    def stats_profit_lost_unit(self, unit_dates):
        sql = '''
        SELECT SUM(profit) as lost_unit FROM evaluation_data
        WHERE profit < 0
        AND trade_date in %s
        '''
        return sql

    @torndb.select
    def stats_profit_lost_max(self):
        sql = '''
        SELECT MIN(profit) as lost_max FROM evaluation_data
        '''
        return sql

    @torndb.select
    def stats_profit_lost_count_total(self):
        sql = '''
        SELECT COUNT(id) as lost_count, SUM(volume) as lost_volume FROM evaluation_data 
        WHERE profit <= 0
        '''
        return sql

    @torndb.select
    def stats_profit_lost_count_unit(self, unit_dates):
        sql = '''
        SELECT COUNT(id) as lost_count, SUM(volume) as lost_volume FROM evaluation_data 
        WHERE profit <= 0
        AND trade_date in %s
        '''

        return sql


    @torndb.select
    def stats_earn_total(self):
        sql = '''
        SELECT (SUM(profit) - SUM(commission)) as earn_sum FROM evaluation_data
        '''
        return sql

    @torndb.select
    def stats_commission_total(self):
        sql = '''
        SELECT SUM(commission) as commission_sum FROM evaluation_data
        '''
        return sql

    @torndb.get
    def stats_commission_unit(self, unit_dates):
        sql = '''
        SELECT SUM(commission) as commission_unit FROM evaluation_data
        WHERE trade_date in %s
        '''
        return sql

    @torndb.select
    def stats_earn_unit(self, unit_dates):
        sql = '''
        SELECT (SUM(profit) - SUM(commission)) as earn_unit FROM evaluation_data
        WHERE trade_date in %s
        '''
        return sql

    @torndb.select
    def stats_unit(self, limit, offset):
        sql = '''
        SELECT DISTINCT trade_date FROM evaluation_data ORDER BY trade_date DESC LIMIT %s OFFSET %s
        '''
        return sql

evaluationStatsDAO = EvaluationStatsDAO()
