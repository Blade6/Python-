# encoding:utf-8
# 装饰器

# def now():
# 	print '2017-01-08'
# 函数对象有一个__name__属性，可以拿到函数的名字
# print now.__name__
# 'now'

# 增加在函数调用前后自动打印日志的功能，但不要改变now()函数的定义
# 装饰器：在代码运行期间动态增加功能
# 定义打印日志的装饰器log
# def log(func):
#     def wrapper(*args, **kw):
#         print 'call %s():' % func.__name__
#         return func(*args, **kw)
#     return wrapper
# 使用python的@语法，把装饰器置于函数的定义处
# @log
# def now():
# 	print '2017-01-08'
# now()
# 结果如下
# call now():
# 2017-01-08
# None
# 解释说明：
# @log相当于执行了语句now = log(now)
# 由于log()是一个decorator，返回一个函数，
# 所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，
# 于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
# wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。
# 在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
# print now.__name__
# 'wrapper'
# 如果要保证原函数名不变，可以增加一句
# @functools.wraps(func)
# 增加在13和14行之间，而且记得写import functools

# 带参数的装饰器
import functools
def log(text):
    def decorator(func):
    	@functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator
@log('execute')
def now():
	print '2017-01-08'
now()
print now.__name__
# 结果如下：
# execute now():
# 2017-01-08
# 解释说明：
# now = log('execute')(now)
# 首先执行log('execute')，返回的是decorator函数，
# 再调用返回的函数，参数是now函数，返回值最终是wrapper函数

# 课后作业：
# import functools
# def log(text=None):
#     def decorator(func):
#     	@functools.wraps(func)
#         def wrapper(*args, **kw):
#             print 'begin call'
#             if isinstance(text,str):
#             	print text
#             re = func(*args, **kw)
#             print 'end call'
#             return re
#         return wrapper
#     return decorator
# @log()
# def f():
# 	print 'Hi'
# f()
# @log('execute')
# def g():
# 	print 'Hello'
# g()