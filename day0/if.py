# -*- coding: utf-8 -*-

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')


s = input("birth:")
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')


# 练习
# 小明身高1.75,体重80kg,请根据BMI公式(体重除以身高的平方)帮小明计算他的BMI指数,并根据BMI指数
# 低于18.5：过轻
# 18.5 - 25：正常
# 25 - 28：过重
# 28 - 32：肥胖
# 高于32：严重肥胖

hegiht = 1.75
weight = 80.5

bmi = weight / (1.75 * 1.75)
print('bmi:' + str(bmi))
if bmi > 32:
    print('严重肥胖')
elif 28 < bmi <= 32:
    print('肥胖')
elif 25 < bmi <= 28:
    print('过重')
elif 18.5 < bmi <= 25:
    print('正常')
elif bmi <= 18.5:
    print('过轻')
