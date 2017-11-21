# 序列化

import pickle

d=dict(name='MuNaiYi',age=30,score=100)
# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
print(pickle.dumps(d))

# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object
# 看到写入的dump.txt文件，一堆乱七八糟的内容，这些都是Python保存的对象内部信息。
def wirteDumpFile():
    with open('./dump.txt','wb') as f:
      pickle.dump(d,f)

#wirteDumpFile()

# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
def deserializationObject():
    with open('./dump.txt','rb') as f:
        d=pickle.load(f)
        return d

print(deserializationObject())
