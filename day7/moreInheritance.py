# 多重继承
# 通过多重继承,一个子类就可以同时获得多个父类的所用功能

class Animal(object):
    pass

# 大类 哺乳动物
class Mammal(Animal):
    pass

# 鸟类
class Brid(Animal):
    pass

class RunnableMixIn(object):
    def run(self):
        print('Running ...')

class FlyableMixIn(object):
    def fly(self):
        print('Flying ...')

# 食肉动物
class CarnivorousMixIn(object):
    pass

 #  食草动物
class HerbivoresMixIn(object):
    pass
    
 # 多重继承
class Dog(Mammal,RunnableMixIn,CarnivorousMixIn):
    pass

# 蝙蝠
class Bat(Mammal,FlyableMixIn):
    pass

# 鹦鹉
class Parrot(Brid):
    pass

# 鸵鸟
class Ostrich(Brid):
    pass


