# -*- coding:utf-8 -*-
# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。

# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling

# Python提供两个模块来实现序列化：cPickle和pickle。这两个模块功能是一样的，
# 区别在于cPickle是C语言写的，速度快，pickle是纯Python写的，速度慢，跟cStringIO和StringIO一个道理。
# 用的时候，先尝试导入cPickle，如果失败，再导入pickle
try:
    import cPickle as pickle
except ImportError:
    import pickle

d = dict(name='Bob', age=20, score=88)
print pickle.dumps(d) 
# pickle.dumps()方法把任意对象序列化成一个str，然后，就可以把这个str写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
# >>> f = open('dump.txt', 'wb')
# >>> pickle.dump(d, f)
# >>> f.close()   
# 看看写入的dump.txt文件，一堆乱七八糟的内容，这些都是Python保存的对象内部信息

# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个str，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。我们打开另一个Python命令行来反序列化刚才保存的对象：

# >>> f = open('dump.txt', 'rb')
# >>> d = pickle.load(f)
# >>> f.close()
# >>> d
# {'age': 20, 'score': 88, 'name': 'Bob'}
# 变量的内容又回来了！

# 当然，这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已。