# encoding:utf-8
# 迭代
d = {'a':1,'b':2,'c':3}
for key in d:
	print key
# you will get a,b,c.Their order may be not sure,because dict is special

for value in d.itervalues():
	print value
# you will get 1,2,3

for k,v in d.iteritems():
	print k,'=>',v

# 判断一个对象是不是可迭代对象
from collections import Iterable
print isinstance('abc', Iterable)
# str是否可迭代
# True

# 使用下标循环访问list
for i, value in enumerate(['a','b','c']):
	print i,value
# 0 a
# 1 b
# 2 c