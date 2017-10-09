# 递归函数

def fact(n):
    if n == 1:
        return n
    return n * fact(n - 1)


result = fact(1)

print('result:', result)

result = fact(5)
print('result:', result)


# 尾递归

def fact1(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


result = fact1(5)
print('尾递归:', result)
