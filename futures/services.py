# -*- coding:utf-8 -*-
from futures.models import itemDAO
from futures.models import nodeDAO
from simpletor.db import transactional

def get_items():
    return itemDAO.all()

def get_default_item():
    return itemDAO.get_default_item()

@transactional
def save_item(item):
    itemDAO.save(**item)

@transactional
def set_default(item_id):
    itemDAO.reset_default()
    itemDAO.set_default(item_id)

@transactional
def remove_item(item_id):
    itemDAO.delete_item(item_id)

def get_nodes():
    nodes = []
    try:
        nodes = nodeDAO.all()
    except:
        pass
    return nodes

@transactional
def save_node(node):
    try:
        n = nodeDAO.find_node(**node)
    except:
        pass
    if n is None or len(n) == 0:
        nodeDAO.save(**node)
    else:
        nodeDAO.update_node(**node)

@transactional
def remove_node(node_id):
    nodeDAO.delete(node_id)