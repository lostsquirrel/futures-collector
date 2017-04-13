# -*- coding:utf-8 -*-

from simpletor import db

class Node(db.Row):
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


class Item(db.Row):
    '''
    Node
    '''
    def __init__(self):
        self.id = None
        self.name = None
        self.status = 0

class ItemDAO:
    '''
    Artist DAO
    '''

    @db.insert
    def save(self, **artisan):
        sql = '''
        INSERT INTO artisan (name) 
        VALUES (%(name)s);
        '''
        return sql

    @db.get
    def find(self, item_id):
        sql = '''
        SELECT id, name, status FROM item a WHERE a.id = %s AND a.status = 0;
        '''
        return sql

    @db.update
    def update_name(self, **artisan):
        sql = '''
            UPDATE item a SET 
            name = %(name)s
            WHERE a.id = %(id)s 
            '''
        return sql

    @db.update
    def update_status(self, **artisan):
        sql = '''
            UPDATE item a SET 
            status = %(status)s
            WHERE a.id = %(id)s 
            '''
        return sql

    @db.select
    def all(self):
        sql = '''
            SELECT id, name, status FROM item WHERE status = 0;
            '''
        return sql

itemDAO = ItemDAO()