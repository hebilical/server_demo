
#打包并且安装


make dist

pip install dist/server_demo-xxxx-.whl


#安装后写好配置文件, 启动命令：


honcho start


# 单元测试 ：


honcho start(先启动服务)



make  test(在另一个终端进行单元测试)
