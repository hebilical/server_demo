# -*- coding: UTF-8 -*-
import os
import peewee
from dateutil.tz import tzlocal
from datetime import datetime
from peewee import AutoField, DateTimeField, SQL
from playhouse.db_url import connect as db_connect

database = db_connect(os.environ.get('DATABASE_URL', None))



class _BaseRecordModel(peewee.Model):
    id_ = AutoField(column_name='id', primary_key=True)
    created_at = DateTimeField(constraints=[SQL('DEFAULT NOW()')])
    updated_at = DateTimeField(constraints=[SQL('DEFAULT NOW()')])

    class Meta:
        database = database

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(tzlocal())
        return super().save(*args, **kwargs)



