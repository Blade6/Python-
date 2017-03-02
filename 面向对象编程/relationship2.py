# -*- coding:utf-8 -*-

# dir()活动二一个对象的所有属性和方法
print dir('ABC')
# 'ABC'是字符串类的一个对象，第四行会打印str的属性和方法
# 其中欧冠类似__xx__的属性和方法都是有特殊用途的
# len('ABC')和'ABC'.__len__()的效果是等价的

class MyObject(object):
	def __len__(self):
		return 100
	def length(self):
		return 100
obj = MyObject()
print len(obj)
print obj.length()

class Myobject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x
obj1 = Myobject()
print hasattr(obj1,'x')
# hasattr()判断对象是否含有某属性
print hasattr(obj1,'power')
# True
setattr(obj1,'y',10)
# setattr()方法设置属性
print getattr(obj1,'y')
print obj1.y
# getattr()方法获取属性，如果属性不存在会报错哦
print getattr(obj1,'z',11)
# 为getattr()方法设置默认值11，如果不存在属性z，则返回11
