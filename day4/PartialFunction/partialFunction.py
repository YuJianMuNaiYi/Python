# 偏函数

import functools
result = int('12345')  # 默认按照十进制转换
print(result)

result = int('12345', base=8)  # 按照八进制转换
print(result)

result = int('12345', base=16)  # 按照十六进制转换
print(result)

# functools.partial帮助我们创建一个偏函数
# functools.partial的作用就是,把一个函数的某些参数给固定住(也就是设置默认值),返回一个新函数,调用这个新函数会更简单
int2 = functools.partial(int, base=2)
result = int2('1000000')
print(result)
result = int2('1010101')
print(result)
result = int2('1000000', base=10)
print(result)
