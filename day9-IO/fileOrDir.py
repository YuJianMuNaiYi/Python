# 操作文件和目录

import os

print(os.name) #操作系统类型   如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
# print(os.uname())  # 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。

# 环境变量
# 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
print(os.environ)
# 要获取某个环境变量的值,可以调用
print('PATH环境变量的值:%s' % os.environ.get('PATH'))

# 操作文件和目录
# 操作文件和目录的函数一部分放在os模块总,一部分放在os.path模块中

# 查看当前目录的绝对路径
print('当前目录的绝对路径:%s' % os.path.abspath('.'))
# 在某个目录下创建一个新目录,首先把新目录的完整路径表示出来
# 把两个路径合成一个时,不要直接拼字符串,而要通过os.path.join()函数,这样可以正确处理不同操作系统的路径分隔符
newDirPath=os.path.join(os.path.abspath('.'),'testDir')
os.mkdir(newDirPath)
# 拆分路径时,也不要直接拆分字符串,而要通过os.path.split()函数,这样可以把一个路径拆分为两部分,后一部分总是最后级别的目录或文件名
os.path.split('/Users/michael/testdir/file.txt')
# 拆分后的路径('/Users/michael/testdir', 'file.txt')

# os.path.splitext()可以直接让你得到文件扩展名
os.path.splitext('/path/to/file.txt')
# ('/path/to/file', '.txt')

#删掉一个目录
os.rmdir(newDirPath)

# 对文件进行重命名
# os.rename('test.txt','test.py')

# 删除文件
# os.remove('test.py')

# shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。

# 过滤文件
files=[x for x in os.listdir('.') if os.path.isdir(x)]
print('文件目录下的所有目录:%s' % files)

pyFiles=[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

print('当前目录下所有后缀为.py的文件:%s' % pyFiles)



