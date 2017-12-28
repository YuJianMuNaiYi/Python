# 常用第三方模块---requests

import requests

#带参数的URL,传入一个dict作为params参数
r=requests.get('https://www.douban.com/',params={'q':'python','cat':'1001'})
# print('statusCode:%s'% r.status_code)
# print('encoding:%s'% r.encoding)
# print(r.text)

# request的方便之处就在于,对特特定类型的响应,例如JSON,可以直接获取

r=requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')

print(r.json())
