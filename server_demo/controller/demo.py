# -*- coding: UTF-8 -*-
from server_demo.model.demo import UserShareTrace


async def trace_new(weibo_id, user_name=0, at_user_list=None):
    if not at_user_list:
        at_user_list = []
    at_user_list = list(set(at_user_list))
    UserShareTrace.create(weibo_id=weibo_id, created_by=user_name, at_user_list=at_user_list)


async def get_suggest_users(user_name,  target_user, page_no=1, page_size=10):
    share_trace = UserShareTrace.select().where(UserShareTrace.created_by == user_name).paginate(page_no, page_size)    
    result = []
    for j in share_trace:
        if target_user in j.at_user_list:
            j.at_user_list.remove(target_user)
        j_set = set(j.at_user_list)
        result_set = set(result)
        diff_set = j_set - result_set
        if diff_set: 
            result.extend(list(diff_set))
    return result
