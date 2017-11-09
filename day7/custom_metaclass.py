# metaclass

class ListMetaClass(type):
    # 参数依次是:
    # 当前准备创建类的对象
    # 类的名字
    # 类继承的父类集合
    # 类的方法集合
    def __new__(cls, name,bases,attrs):
            attrs['add']=lambda self,value:self.append(value)
            return type.__new__(cls,name,bases,attrs)


class MyList(list,metaclass=ListMetaClass):
    pass

