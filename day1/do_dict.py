d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])


# 判断dict类型的d 中是否存在liu,如果不存在则添加
if not 'liu' in d:
    d['liu'] = 100

for item in d:
    print(item)

print(d.get('liu'))
print(d.get('zhangSan', -1))

for item in d:
    print(item)
