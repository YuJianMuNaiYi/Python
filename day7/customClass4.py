# 定制类

class Chain(object):
    def __init__(self,path=''):
        self._path=path
    def __getattr__(self, path):
         return Chain('%s/%s' %(self._path,path))

    def __str__(self):
        return  self._path

    # __repr=__str__

path=Chain().status.user.timeLine.list
print('path:%s'% path)
