s = set([1, 2, 3])

print(s)

# 重复元素在set中自动被过滤

t = set([1, 1, 2, 2, 3, 3, 4, 5, 6])
print(t)

# 添加元素
t.add(7)
t.add(3)
t.add(8)

t.add(7)

print(t)

# 移除元素
t.remove(3)
print(t)


# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作

print(s & t)
