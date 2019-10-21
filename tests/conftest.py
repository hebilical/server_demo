import os
import pytest
import importlib
import requests
import threading
from tornado.web import Application
from tornado.ioloop import IOLoop
import logging


LOG = logging.getLogger()


def db_init():
    module = importlib.import_module('.', 'server_demo.model')
    md = module.__dict__
    files = os.listdir(md['__path__'][0])
    model_list = []
    for i in files:
        if   i.startswith('__') is False:
            table_module = importlib.import_module('.', f'server_demo.model.{i[:-3]}')
            table_md = table_module.__dict__
            simple_list = [
            table_md[c] for c in table_md if (
            isinstance(table_md[c], type) and table_md[c].__module__ == table_module.__name__)]
            model_list.extend(simple_list)
    for model in model_list:
        print(model.__dict__)
        LOG.warning(f'ready to truncate table {model.__name__}')
        model.truncate_table()


class TestClient():
    base_url = 'http://127.0.0.1:8000'
    def post(self,url=None, json={}, data={}):
        if not url :
            return None
        if json:
            headers = {'Content-Type': 'application/json'}
            return requests.post(self.base_url+url, json=json, data=data, headers=headers)
        else:
            return requests.post(self.base_url+url, json=json, data=data, headers=headers)
    
    def get(self, url, params=None):
        if not url:
            return None
        return requests.get(self.base_url+url, params=params)
    
   
    def client(self):
        db_init()


@pytest.fixture()
def client():
    client = TestClient()
    client.client()
    return client
