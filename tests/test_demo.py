import pytest

def test_demo(client):
    url = '/postWeibo'
    data = dict(userName='AAA', weiBoId=1, atUserList=['bbbb'])
    resp = client.post(url, json=data)