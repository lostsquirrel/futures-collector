# -*- coding:utf-8 -*-


from torndb import Connection

class Row(dict):
    """A dict that allows for object-like property access syntax."""    
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)
        
    def __setattr__(self, name, value):
        self[name] = value



import settings

torcon = Connection(settings.db_host, settings.db_name, user=settings.db_user, password=settings.db_pass)

def transactional(method):
    result = None
    def wrapper(*args, **kwds):
        try:
            result = method(*args, **kwds)
            torcon._db.commit()
        except Exception, e:
            torcon._db.rollback()
            raise e
        return result
    return wrapper

def get(method):
    def wrapper(dao, *args, **kwds):
        sql = method(dao, *args, **kwds)
        return torcon.get(sql, *args, **kwds)
    return wrapper
    
def select(method):
    def wrapper(dao, *args, **kwds):
        sql = method(dao, *args, **kwds)
        return torcon.query(sql, *args, **kwds)
    return wrapper

def insert(method):
    def wrapper(dao, *args, **kwds):
        sql = method(dao, *args, **kwds)
        return torcon.insert(sql, *args, **kwds)
    return wrapper

def update(method):
    def wrapper(dao, *args, **kwds):
        sql = method(dao, *args, **kwds)
        return torcon.update(sql, *args, **kwds)
    return wrapper

def delete(method):
    def wrapper(dao, *args, **kwds):
        sql = method(dao, *args, **kwds)
        return torcon.execute(sql, *args, **kwds)
    return wrapper
