# encoding:utf-8
# 列表生成式

print range(1,11)
# [1,2,3,4,5,6,7,8,9,10]

# 生成[1*1,2*2,...10*10]可以写循环，但循环太麻烦，使用下式即可
L = [x * x for x in range(1,11)]
print L

# 还可以加上if判断
L = [x * x for x in range(1,11) if x % 2 == 0]
print L

# 还可以使用两层循环
S = [m + n for m in 'ABC' for n in 'XYZ']
print S
# ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

# 列出当前目录下的所有文件和目录名
import os
print [d for d in os.listdir('.')]

# 生成字符串List
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print [k + '=' + v for k, v in d.iteritems()]
# ['y=B', 'x=A', 'z=C']

# 把字符串转为小写
L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]
# ['hello', 'world', 'ibm', 'apple']

L = ['Hello', 'World', 18, 'Apple', None]
print [s.lower() for s in L if isinstance(s,str)]
# ['hello', 'world', 'apple']