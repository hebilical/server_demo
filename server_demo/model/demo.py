# -*- coding: UTF-8 -*-
from server_demo.common.base import _BaseRecordModel
from peewee import IntegerField, CharField
from playhouse.postgres_ext import ArrayField


class   UserShareTrace(_BaseRecordModel):
    weibo_id = IntegerField()
    created_by = CharField()
    at_user_list = ArrayField()

    class Meta:
        table_name = 'user_share_trace'