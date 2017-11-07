# 使用@propery
# @propery广泛应用在类的定义中,可以让调用者写出简短的代码,同时保证对参数进行必要的检查,这样程序运行时就就减少了出错的可能性

class Student(object):
    def get_score(self):
        return self.score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value<0 or value>100:
            raise ValueError('score must between 0 ~ 100!')
        self.score = value

s=Student()
s.set_score(99)
print('score:%s' % s.get_score())
# s.set_score(999)
# print('score:%s' % s.get_score()) # ValueError: score must between 0 ~ 100!


# 简单方式
class Student1(object):
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value<0 or value>100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
        
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,value):
        self._birth=value

    # 增加只读属性
    @property
    def age(self):
        return 2017-self._birth
    
s1=Student1()
s1.score=90
print('@property score:%s' % s1.score)

# 1.score=999 # ValueError: score must between 0 ~ 100!
# print('@property score:%s' % s1.score)

class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        self._width=value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        self._height=value

    @property
    def resolution(self):
        return self._width * self._height
