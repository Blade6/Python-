# -*- coding:utf-8 -*-

# 判断继承关系
class Animal(object):
	pass
class Dog(Animal):
	pass
class Husky(Dog):
	pass
a = Animal()
d = Dog()
h = Husky()
print isinstance(h,Husky)
print isinstance(h,Dog)
print isinstance(h,Animal)


# type()：判断对象类型
print type(123)
# <type 'int'>
print type('str')
# <type 'str'>
print type(None)
# <type 'NoneType'>

# 判断类或方法
print type(abs)
# <type 'builtin_function_or_method'>

class Animal:
	pass

print type(Animal)
# <type 'classobj'>

print type(123)==type(456)
# True

import types
print type('abc')==types.StringType
print type(u'abc')==types.UnicodeType
print type([])==types.ListType

print type(str)==types.TypeType
# 所有类型本身的类型就是TypeType