# encoding:utf-8
# filter()接收一个函数和一个序列
# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素

# 删除序列中的偶数
def is_odd(n):
    return n % 2 == 1

print filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])
# [1, 5, 9, 15]

def not_empty(s):
    return s and s.strip()
# s.strip()返回去除掉空格的字符串
# s.strip('x')返回去除掉所有小写字母x的字符串

print filter(not_empty, ['A', '', 'B', None, 'C', '  '])
# ['A', 'B', 'C']

# 删除1-100的素数
from math import sqrt
def isNotPrime(x):
	if(x==1):
		return True
	else:
		for n in range(2,int(sqrt(x))+1):
			if(x % n == 0):
				return True
		return False
print filter(isNotPrime,range(1,101))