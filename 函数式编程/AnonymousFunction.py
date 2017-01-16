# encoding:utf-8
# 匿名函数

# 计算f(x)=x^2
print map(lambda x: x * x, range(1,10))
# lambda x: x * x 实际上就是下面这个函数
# def f(x):
#     return x * x
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数
# 匿名函数优点：
# 1.不用担心函数名冲突
# 2.匿名函数可赋值给变量，通过变量来调用；也可以作为返回值返回
# Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数