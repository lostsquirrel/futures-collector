# -*- coding:utf-8 -*-

from evaluation.models import evaluationDataDAO as dataDAO
from simpletor.torndb import transactional

@transactional
def save_data(data):
    dataDAO.save(**data)

def get_all_data():
    return dataDAO.find_all()

@transactional
def remove_data(data_id):
    dataDAO.remove(data_id)