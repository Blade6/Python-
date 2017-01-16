# encoding:utf-8
def nop():
	pass
# empty function,pass是占位符，保证不报错，以后想到函数逻辑再写代码

age = 21
if age >= 18:
	pass
# pass can also use in if/else sentence

def lalala(x,y):
	return x+1,y+1
#python可以返回多个值，而java、C++、php都不行

x, y = lalala(12,13)
print x, y 
# 13,14
r = lalala(13,14)
print r
# (14,15)


# 默认参数
def what(name,city='Beijing'):
	print 'name:',name,'city:',city
what('Blade6')
what('Jesus','Heaven')
# 默认参数的坑
def add_end(L=[]):
    L.append('END')
    return L
print add_end([1, 2, 3])
# [1, 2, 3, 'END']
print add_end()
# ['END']
print add_end
# ['END', 'END'] ===>不对了
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
# 因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
# 定义默认参数要牢记一点：默认参数必须指向不变对象！

# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# print calc([1,2,3])
# print calc((1,3,5,7))
# 调用的时候需要先组装list或turple
# 可变参数
# *numbers是turple类型
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
# *numbers表示可变参数，参数可能是1个，也可能0个，可能很多
print calc(1,2,3)
L = [1,2,3]
print calc(*L)
# 如果已经有list或turple了，传入参数前面加上*即可


# 关键字参数
# **kw是dict类型
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw
person('Bob',30)
# name: Michael age: 30 other: {}
person('Bob', 35, city='Beijing')
# name: Bob age: 35 other: {'city': 'Beijing'}
d = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack',24,**d)
# name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
# 如果已经有dict了，传入参数前面加上**即可


# 在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，
# 这4种参数都可以一起使用，或者只用其中某些，但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。
# 如果普通参数、默认参数、可变参数、关键字参数同时出现的话
def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
func(1, 2)
# a = 1 b = 2 c = 0 args = () kw = {}
func(1, 2, c=3)
# a = 1 b = 2 c = 3 args = () kw = {}
func(1, 2, 3, 'a', 'b')
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
func(1, 2, 3, 'a', 'b', x=99)
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
args = (1, 2, 3, 4)
kw = {'x': 99}
func(*args, **kw)
# a = 1 b = 2 c = 3 args = (4,) kw = {'x': 99}
# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。