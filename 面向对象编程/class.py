# -*- coding:utf-8 -*-
# 类
class Student(object):

	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print '%s: %s' % (self.name, self.score)

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的
# __init__方法的第一个参数永远是self，表示创建的实例本身，
# 因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身

# 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数
