#负责启动WSGI服务器,加载application()函数
from wsgiref.simple_server import make_server
from test_wsgi_hello import application

#创建一个服务器,IP地址为空,端口是8000,处理函数是application
httpd=make_server('',8000,application)
print('Serving Http on port 8000 ...')

#开始监听HTTP请求
httpd.serve_forever()
