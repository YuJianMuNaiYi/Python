# 枚举
from enum import Enum,unique

# @unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
    

print(Weekday.Mon)
print(Weekday.Mon.value)
print(Weekday.Sat.value)
