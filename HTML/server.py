#启动服务器，加载application()函数
#wsigiref模块导入
#导入我们自己编写的application函数
from hello import application
from wsgiref.simple_server import make_server
#创建一个服务器，ip地址为空，端口是8000,处理函数是application
httpd=make_server('',8000,application)
print('Serving HTTP on port 8000...')
#开始监听HTTP请求
httpd.serve_forever()