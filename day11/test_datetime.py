# Python内建的模块---datetime
# 注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。
# 如果仅导入import datetime，则必须引用全名datetime.datetime。
# datetime.now()返回当前日期和时间，其类型是datetime。

from datetime import  datetime,timedelta,timezone

# 获取当前日期和时间
now=datetime.now()
print('当前时间:%s' % now)

print(type(now))

# 获取指定日期和时间
#要指定某个日期和时间,我们直接用参数构造一个datetime

dt=datetime(2017,12,12,23,00)
print(dt)

# datetime转换为timestamp
# timestamp的值与时区毫无关系,因为timestamp一旦确定,其UTC时间就确定了,转换到任意时区的时间也是完全正确的,这就是为什么计算机存储的当前时间是以timestamp表示的,因为全球各地的计算机在任意时刻的timestamp都是完全相同的

dt=datetime(2015,4,19,12,20)
ts=dt.timestamp()
print(ts) # 注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
# 某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。

#timestamp转换为datetime
#要把timestamp转换为timestamp,使用datetime提供的fromttimestamp()方法

t=1429417200.0
d=datetime.fromtimestamp(t)    #本地时间
print(d)

u=datetime.utcfromtimestamp(t) #UTC时间
print(u)

# str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime转换为str

n=datetime.now()
print(n.strftime('%a, %b %d %H:%M'))

# datetime加减
# 使用timedelta你可以很容易地算出前几天和后几天的时刻。
tempNow=datetime.now()
r=tempNow+timedelta(hours=10)
print(r)
d=tempNow+timedelta(days=1)
print(d)

d=tempNow+timedelta(days=2,hours=12)
print(d)

# 本地时间转换为UTC时间
# 一个datetime类型有一个时区属性tzinfo,但是默认为None,所以无法区分这个datetime到底是哪个时区,除非强行给datetime设置一个时区

tz_utc_8=timezone(timedelta(hours=8)) #创建时区UTC+8:00
print(tz_utc_8)

now=datetime.now()

dt=now.replace(tzinfo=tz_utc_8)
print(dt)

# 时区转换
# 可以先通过utcnow()取的当前的UTC时间,再转换为任意时区的UTC时间

#取得UTC时间,并强制设置时区为UTC+0:00:
utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)

# astimezone()将转换时区为北京时间:
bj_dt=utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

# astimezone()将转换时区为东京时间:
tokyo_dt=utc_dt.astimezone(timezone(timedelta(hours=9)))
print('东京时间:%s' % tokyo_dt)

# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2=bj_dt.astimezone(timezone(timedelta(hours=9)))
print('北京时间转换为东京时间:%s' % tokyo_dt2)

# 时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
# 利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。






