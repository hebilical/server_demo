
#打包并且安装


make dist

pip install dist/server_demo-xxxx-.whl


#安装后制定配置文件和bin：


honcho -e /home/myuser/code/server_demo/.env  run  /home/myuser/code/server_demo/venv/bin/server-demo

