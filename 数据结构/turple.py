# encoding:utf-8
classmates = ('Michael','Bob','Nancy')

# tuple一旦初始化，不能修改（包括增加，修改），其他和list相同

t = ()
# empty turple

t = (1, 2)
print t
# (1,2)

t = (1)
# in this case, t is not a turple, t is int 1.
# 因为()既可以表示turple，也可以表示数学运算，此种情况下，Python规定为数学运算
# to get a turple with only an element,you should do it this way:
t = (1,)
print t
# (1,)

t = ('a', 'b', ['A','B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print t
# ('a', 'b', ['X','Y'])
# turple can't be change,but list can.
# list的内存位置没变，只是指向的内容变了