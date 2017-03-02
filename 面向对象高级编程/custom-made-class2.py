# -*- coding:utf-8 -*-
# 定制类
class Student(object):
	def __init__(self):
		self.name = 'Michael'

s = Student()
print s.name
# 'Michael'
# print s.score
# you get an error

# you can add an score into  __init__() or do it like the following lines
class Student2(object):
	def __init__(self):
		self.name = 'Michael'

	def __getattr__(self, attr):
		if attr == 'score':
			return 99
		elif attr == 'age':
			# return an function
			return lambda: 26
		else :
			raise AttibuteError('\'Student\' object has no attribute \'%s\'' % attr)

s1 = Student2()
print s1.score
print s1.age()

# 任何类，定义一个 __call__()方法，就可以直接对实例进行调用
class Student3(object):
	def __init__(self, name):
		self.name = name

	def __call__(self):
		print('My name is %s.' % self.name)

s2 = Student3('Michael')
s2()

# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
print callable(Student2())
print callable(max)
print callable(None)
print callable('string')
print callable([1,2,3])