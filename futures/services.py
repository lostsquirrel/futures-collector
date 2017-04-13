# -*- coding:utf-8 -*-
from futures.models import itemDAO

def get_items():
    return itemDAO.all()