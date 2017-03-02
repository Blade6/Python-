# -*- coding:utf-8 -*-
# metaclass 元类
# 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
# 但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
# 换句话说，你可以把类看成是metaclass创建出来的“实例”。

# 按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass
# metaclass是创建类，所以必须从`type`类型派生
class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value: self.append(value)
		return type.__new__(cls, name, bases, attrs)

# __new__()方法接收到的参数依次是：
# 当前准备创建的类的对象；
# 类的名字；
# 类继承的父类集合；
# 类的方法集合。

class MyList(list):
	# 指示使用ListMetaclass来定制类
	__metaclass__ = ListMetaclass

L = MyList()
L.add(1)
print L
# [1]