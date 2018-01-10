#网络编程---UDP---服务端
import socket

#SOCK_DGRAM指定了这个Socket的类型是UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#绑定端口
s.bind(('127.0.0.1',9999))

print('Bind UDP on 9999...')
print("Welcome...")
while True:
    #接收数据
    #返回数据和客户端的地址与端口
    data,addr=s.recvfrom(1024)
    print('Received from %s:%s.'% addr)
    #将数据用UDP发给客户端
    s.sendto(b'Hello,%s!'% data,addr)
