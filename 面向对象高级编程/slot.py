# -*- coding:utf-8 -*-
class Student(object):
	pass

s = Student()

# 动态给类绑定方法
def set_score(self, score):
	self.score = score
Student.set_score = MethodType(set_score, None, Student)

s.set_score(88)
print s.score

s.name = 'Lilei'
# 如果想限制类的属性
class Student1(object):
	# 用tuple定义
	__slot__ = ('name', 'age')
# __slot__仅对当前类起作用，子类需要另外定义

s1 = Studnet1()
s1.score = 99 
# 报错，因为__slot__中没有包含score，所以不能绑定score属性