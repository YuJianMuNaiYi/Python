# 返回函数

def calc_sum( *args):
    def sum1():
        r = 0
        for n in args:
            r += n
        return r
    return sum1

f1 = calc_sum(1,3,5,7,9) # 此时返回的并不是求和结果,而是求和函数
f2 = calc_sum(1,3,5,7,9) # 当调用calc_sum时,每次调用都会返回一个新的函数,即使传入的参数是相同的,所以此处的f1!=f2

print(f1())

print(f1 == f2)

