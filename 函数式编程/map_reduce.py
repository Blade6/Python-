# encoding:utf-8
# map()函数:接收两个参数，一个是函数，一个是序列。
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。
def f(x):
	return x * x
print map(f,range(1,10))
# [1, 4, 9, 16, 25, 36, 49, 64, 81]
# 当然，这里用列表生成式一行代码就可以实现。map()可以用在更厉害的场合
print map(str,range(1,10))
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# reduce()函数:接收两个参数，一个是函数F，一个是序列。
# 把函数F作用在序列[x1, x2, x3...]上.
# 函数F必须接收两个参数，reduce()把结果继续和序列的下一个元素做累积计算
# reduce()首先把用函数F计算x1,x2，F计算完返回结果
# 然后reduce()把结果和x3代入F计算...以此类推
def fn(x,y):
	return x * 10 + y
print reduce(fn,range(1,6))
# 12345

# 编写字符串转整型的函数
def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print reduce(fn,map(char2num,range(1,6)))
# 12345
# 把这个函数做些处理，使它能更通用
# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y
#     def char2num(s):
#         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#     return reduce(fn, map(char2num, s))
# 这样就能调用str2int(str)了

names = ['adam', 'LISA', 'barT']
# 将字符串规范化为首字母大写，其他小写
print map(str.capitalize,names)
# map(str.lower,names)将字符串转化为小写

L = range(1,11)
# sum函数求和
print sum(L)

# prod函数求积
def prod(l):
	def f(x,y):
		return x * y
	return reduce(f,l)
print prod(L)