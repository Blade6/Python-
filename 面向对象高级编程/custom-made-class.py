# -*- coding:utf-8 -*-
# 定制类
class Student(object):
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return 'Student object (name: %s)' % self.name

s = Student('Michael')
print s
# Student object (name: Michael)

# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个 __iter__()方法，
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的 next() 方法拿到循环的下一个值，
# 直到遇到StopIteration错误时退出循环

# 斐波那契数列
class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1
	
	def __iter__(self):
		# 变量本身就是迭代对象的话，就返回自己
		return self

	def next(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 100000:
			# 结束循环
			raise StopIteration()
		return self.a

for n in Fib():
	print n

# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行
# 要表现得像list那样按照下标取出元素，需要实现 __getitem__()方法

class Fib_1(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

f = Fib_1()
print f[0],f[10],f[100]

# 添加简单切片功能
class Fib_2(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

ff = Fib_2()
print ff[0:5]
print ff[:10]            

