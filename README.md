
#打包并且安装


make dist

pip install dist/server_demo-xxxx-.whl


#安装后制定配置文件和bin：


honcho -e /home/myuser/code/server_demo/.env  run  /home/myuser/code/server_demo/venv/bin/server-demo


#接口


'http://qjeq5x.natappfree.cc/postWeibo' method: post   json: {"userName": "userA","weiBoId": "3", "atUserList":["userC", "userD"]}



'http://qjeq5x.natappfree.cc/suggest?targetUsersName=userB&userName=userA'  method: get