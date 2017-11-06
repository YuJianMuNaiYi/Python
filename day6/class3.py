# 面向对象编程---类---继承和多态

# 表示该类是从object继承而来的
class Animal(object):
    def run(self):
        print('Animal is running ...')

class Dog(Animal):
    # 也可以对子类增加一些方法
    def run(self):
        print('Dog is running ...')

    def Eat(self):
        print('Eating meat ...')

class Cat(Animal):
    def run(self):
        print('Cat is running ...')

dog=Dog()
dog.run()
dog.Eat()

cat=Cat()
cat.run()





