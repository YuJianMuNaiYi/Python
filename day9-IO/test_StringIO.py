# StringIO顾名思义就是在内存中读写str

from io import StringIO

f=StringIO()
f.write('hello')

print(f.getvalue())  # getvalue()方法用于获得写入后的str。

# 读取StringIO

s=StringIO('Hello!\nHi!\nGoodbye!')
while True:
    line=s.readline()
    if line =='':
        break
    print(line.strip())
