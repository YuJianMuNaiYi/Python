classmates = ['zhangSan', 'liSi', 'wangWu']
print(classmates)

print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[2])
# print(classmates[3]) 所以超出范围


classmates.append('Admin')
print(classmates)

classmates.insert(1, 'MuNaiYi')  # 将元素插入到指定的位置,在此处在索引为1的位置插入
print(classmates)

# 对list进行排序
a = ['c', 'b', 'a']

b = a.sort()

print(b[0])
print(b[1])
print(b[2])
