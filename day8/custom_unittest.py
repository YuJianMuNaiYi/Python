# 单元测试
import unittest         #单元测试需要用到的

class CustomDict(dict):
    def __init__(self,**kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'CustomDice' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key]=value

class TestCustomDict(unittest.TestCase):

    def test_init(self):
        d=CustomDict(a=1,b='test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertEqual(isinstance(d,CustomDict))

    def test_key(self):
        d=CustomDict()
        d['key']='value'
        self.assertEqual(d.key,'value')

    def test_attr(self):
        d=CustomDict()
        d.key='value'
        self.assertTrue('key' in d)
        self.assertEqual(self['key'],'value')

    def test_keyerror(self):
        d=CustomDict()
        with self.assertRaises(KeyError):
            value=d['empty']


    def test_attrerror(self):
        d=CustomDict()
        with self.assertRaises(AttributeError):
            value=d.empty

    # 在测试方法被调用之前调用
    def setUp(self):
        print('setUp...')

    # 在测试方法被调用之后调用
    def tearDown(self):
        print('tearDown...')

if __name__=='__main__':
    unittest.main()

        

        
