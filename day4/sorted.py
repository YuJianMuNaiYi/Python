# 排序

# sorted函数是一个高阶函数,它还可以接受一个key函数来实现自定义的排序
RESULT = sorted([36, 5, -12, 9, -21], key =abs)
print(RESULT)

# 对字符串进行排序
value = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(value)

# 对字符串进行反向排序
value = sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower, reverse=True)
print(value)

# 用一组tuple表示学生名字和成绩
# 用sorted()分别按名字和成绩排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def byname (t):
    def is_str(s):
        return isinstance(s, str)
    r = filter(is_str, t)
    return list(r)[0]

v = sorted(L,key = byname)
print(v)

def byage(t):
    def isnumber(n):
        return isinstance(n,int)
    r=filter(isnumber,t)
    return list(r)[0]
v = sorted(L,key = byage)
print(v)




