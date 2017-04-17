# -*- coding:utf-8 -*-

from simpletor import torndb


class Node(torndb.Row):
    '''
    Node
    '''
    def __init__(self):
        self.id = None
        self.open = None
        self.close = None
        self.lowest = None
        self.highest = None
        self.item_id = None
        self.date = None


class Item(torndb.Row):
    '''
    Node
    '''
    def __init__(self):
        self.id = None
        self.name = None
        self.status = None  # NULL 初始， 1, 默认 9，删除

class ItemDAO:
    '''
    ItemDAO DAO
    '''

    @torndb.insert
    def save(self, **item):
        sql = '''
        INSERT INTO item (name) 
        VALUES (%(name)s);
        '''
        return sql

    @torndb.get
    def find(self, item_id):
        sql = '''
        SELECT id, name, status FROM item a WHERE a.id = %s;
        '''
        return sql

    @torndb.get
    def get_default_item(self,):
        sql = '''
        SELECT id, name, status FROM item a WHERE a.status = 1;
        '''
        return sql

    @torndb.update
    def update_name(self, **item):
        sql = '''
            UPDATE item a SET 
            name = %(name)s
            WHERE a.id = %(id)s 
            '''
        return sql

    @torndb.delete
    def delete_item(self, item_id):
        sql = '''
        DELETE FROM item WHERE id = %s
        '''
        return sql

    @torndb.update
    def set_default(self, item_id):
        sql = '''
            UPDATE item a SET 
            status = 1
            WHERE a.id = %s 
            '''
        return sql

    @torndb.update
    def reset_default(self):
        sql = '''
        UPDATE item a SET 
            status = NULL
            WHERE a.status = 1
        '''
        return sql

    @torndb.select
    def all(self):
        sql = '''
            SELECT id, name, status FROM item;
            '''
        return sql

itemDAO = ItemDAO()

class NodeDAO:


    @torndb.insert
    def save(self, **node):
        sql = '''
        INSERT INTO node (
            open,
            close,
            lowest,
            highest,
            item_id,
            date
            )
        VALUES
        (
        %(open)s,
        %(close)s,
        %(lowest)s,
        %(highest)s,
        %(item_id)s,
        %(date)s
        );    
        '''
        return sql

    @torndb.select
    def all(self):
        sql = '''
             SELECT id,
                open,
                close,
                lowest,
                highest,
                item_id,
                date 
                FROM node WHERE item_id =  (SELECT id FROM item WHERE status = 1) ORDER BY date ASC;
             '''
        return sql

    @torndb.delete
    def delete(self, node_id):
        sql = '''
        DELETE FROM node WHERE id = %s;
        '''
        return sql

    @torndb.select
    def find_node(self, **node):
        sql = '''
        SELECT 
                id,
                open,
                close,
                lowest,
                highest,
                item_id,
                date  
        FROM node a WHERE a.item_id = %(item_id)s AND a.date = %(date)s;
        '''
        return sql

    @torndb.update
    def update_node(self, **node):
        sql = '''
        UPDATE node 
        SET open = %(open)s,
        close = %(close)s,
        lowest = %(lowest)s,
        highest = %(highest)s
        WHERE item_id = %(item_id)s AND date = %(date)s
        '''
        return  sql

nodeDAO = NodeDAO()