# -*- coding: UTF-8 -*-
from server_demo.common.schema import schema
from server_demo.schema.demo import user_schare
from server_demo.controller.demo import trace_new,  get_suggest_users
from server_demo.common.base import _BaseHandler

class DemoHandler(_BaseHandler):
    route = '/postWeibo'

    @schema(json=user_schare, reply=True)
    async def post(self, json):
        await trace_new(json.get('weiBoId', 0), user_name=json.get('userName', ''), at_user_list=json.get('atUserList', []))
        return dict(data='success')


class GetShareUser(_BaseHandler):
    route = '/suggest'

    @schema(query=user_schare, reply=True)
    async def get(self, query):
        data = await get_suggest_users(query.get('userName',''), query.get('targetUserName',''))
        return dict(data=data) 
