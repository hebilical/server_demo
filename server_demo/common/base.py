# -*- coding: UTF-8 -*-
import os
import peewee
from dateutil.tz import tzlocal
from datetime import datetime
from peewee import AutoField, DateTimeField, SQL
from playhouse.db_url import connect as db_connect
from tornado.web import RequestHandler


class Single(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance
    def __init__(self, *arges, **kw):
        pass


class  DataBase(Single):
    def __init__(self):
            db_url = os.environ.get('DATABASE_URL', None)
            self.conn_db = db_connect(db_url)

    @property    
    def database(self):
        return self.conn_db


database = DataBase().database



class _BaseRecordModel(peewee.Model):
    id_ = AutoField(column_name='id', primary_key=True)
    created_at = DateTimeField(constraints=[SQL('DEFAULT NOW()')])
    updated_at = DateTimeField(constraints=[SQL('DEFAULT NOW()')])

    class Meta:
        database = database

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(tzlocal())
        return super().save(*args, **kwargs)



class   _BaseHandler(RequestHandler):
    def on_finish(self, *arg, **kwargs):
        database.close()



