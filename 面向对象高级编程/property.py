# -*- coding:utf-8 -*-
# property的功能类似于函数的装饰器decorater
class Student(object):
	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		self._score = value

s = Student()
s.score = 60
# 实际执行的是s.set_score(60)
print s.score
# 实际执行的是s.get_score()

# 如果只写property而不懈xxx.setter，设置的是只读属性，只能读，不能修改值