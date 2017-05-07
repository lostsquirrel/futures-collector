# -*- coding:utf-8 -*-
from __future__ import print_function
from __future__ import print_function
import re
from simpletor.torndb import transactional
from evaluation.models import evaluationDataDAO as dataDAO
from evaluation.models import evaluationStatsDAO as statsDAO

@transactional
def save_data(data):
    dataDAO.save(**data)

def get_all_data():
    data_list = dataDAO.find_all()
    return data_list

@transactional
def remove_data(data_id):
    dataDAO.remove(data_id)

def get_stats_general():
    data = dict()
    unit_dates = get_unit_dates(5, 0)
    data.update(*statsDAO.stats_profit_win())
    data.update(*statsDAO.stats_profit_win_max())
    data.update(*statsDAO.stats_profit_win_count_total())
    data.update(*statsDAO.stats_profit_win_count_unit(unit_dates))
    data.update(*statsDAO.stats_profit_lost())
    data.update(*statsDAO.stats_profit_lost_max())
    data.update(*statsDAO.stats_profit_lost_count_total())
    data.update(*statsDAO.stats_profit_lost_count_unit(unit_dates))
    data.update(*statsDAO.stats_commission_total())
    data['earn_sum'] = get_earn_sum(data)
    data['win_rate'] = get_win_rate(data)
    return data


def get_earn_sum(data):
    return data['win_sum'] + data['lost_sum'] - data['commission_sum']


def get_win_rate(data):
    return float(100) * data['win_count'] / (data['win_count'] + data['lost_count'])


def get_unit_dates(limit, offset):
    unit_dates = []
    for d in statsDAO.stats_unit(limit, offset):
        unit_dates.append(d.trade_date.strftime('%Y-%m-%d'))
    return unit_dates


def get_stats_unit(unit_num=5):
    limit = 5
    data_list = []
    for x in range(unit_num):
        data = dict()
        offset = x * limit
        unit_dates = get_unit_dates(limit, offset)
        if len(unit_dates) == 0:
            break
        data['unit_start'] = unit_dates[0]
        data['unit_end'] = unit_dates[-1]
        data.update(*statsDAO.stats_profit_win_count_unit(unit_dates))
        data.update(*statsDAO.stats_profit_lost_count_unit(unit_dates))
        data.update(*statsDAO.stats_earn_unit(unit_dates))

        data['win_rate'] = get_win_rate(data)
        data_list.append(data)

    return data_list

if __name__ == '__main__':
    pass