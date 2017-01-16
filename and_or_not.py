# encoding:utf-8
# 与、或、非
# Python中的False value:
# None
# False
# zero of any numeric type, for example, 0,0.0
# any empty sequence, for example, '', (), []
# any empty mapping, for example, {}
# instances of user-defined classes, if the class defines a __nonzero__() or __len__() method,
#  when that method returns the integer zero or bool value False. 
# Operation	Result                                    都是从左往右运算的
# x or y	if x is false, then y, else x	          输出第一个为true的值,如果没有为true的,输出最后一个值为false的
# x and y	if x is false, then x, else y	          输出第一个为false的值，如果没有为false的，输出最后一个值为true的
# not x	    if x is false, then True, else False      
# 注意:and、or运算都是从左往右算的，如果第一个数已经得出结果的话，就不会计算第二个数的！
# 所以filter.py中的None and None.strip() 会得到None
# None.strip()不报错（s.strip()要求s是字符串），因为不会去执行它。

print 'a' and 'b'
# because 'a' is not false,so it output 'b'

print 0 or 3
# because 0 is false,so it output 3
