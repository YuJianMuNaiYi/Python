# 常用第三方模块---psutil
# process and system utilities

import psutil

print('CPU逻辑数量:%s'% psutil.cpu_count())
# 2说明是双核超线程, 4则是4核非超线程
print('CPU物理核心:%s'% psutil.cpu_count(logical=False))
# 统计CPU的用户/系统/空闲时间
print(psutil.cpu_times())

#实现类型top命令的CPU使用率,每秒刷新一次,累计10次
for x in range(10):
    print(psutil.cpu_percent(interval=1,percpu=True))

# 获取内存信息
# 物理内存
print(psutil.virtual_memory())
#交换内存
print(psutil.swap_memory())

#获取磁盘信息
#磁盘分区信息
print(psutil.disk_partitions())
#磁盘使用情况
print(psutil.disk_usage('/'))


#获取网络信息
#获取网络读写字节/包的个数
print(psutil.net_io_counters())
#获取网络接口信息
print(psutil.net_if_addrs())
#获取网络接口状态
print(psutil.net_if_stats())
#获取当前网络连接信息
print(psutil.net_connections())

#获取进程信息
#所有进程ID
ids=psutil.pids()
for id in ids:
    p=psutil.Process(id)
    print('id:%s,name:%s'% (id,p.name()))
print(ids)

# psutil提供的test()函数,可以模拟出ps命令的效果
print(psutil.test())
