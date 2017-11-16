# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
from io import BytesIO

f=BytesIO()
f.write('中文'.encode('utf-8')) # 写入的不是str，而是经过UTF-8编码的bytes。

print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
