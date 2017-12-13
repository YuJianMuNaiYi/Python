# Python内建模块---Base64
# Python内置的base64可以直接进行base64的编解码

import base64

b=base64.b64encode(b'binary\x00string')
print(b)

d=base64.b64decode(b)
print(d)

# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_

r=base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(r)
us=base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(us)

dus=base64.urlsafe_b64decode(us)
print(dus)
