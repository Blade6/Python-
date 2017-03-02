# -*- coding:utf-8 -*-
# python的functools模块提供了很多功能
# 偏函数
print int('12345')
# 12345
print int('12345',base=8)
# 5349
# base值设定输入为8进制，默认为10进制输入
# 输出的都是10进制数
# 第一个参数必须是字符串，如果带base的话。

# def int2(x,base=2):
# 	return int(x,base)
# 编写二进制函数，省去每次都输入2的麻烦
# functools.partial模块能帮助用户省去编写此类函数的麻烦
import functools
int2 = functools.partial(int, base=2)
# 等价于设定了默认值为2，不再是10了
print int2('1000000')
# 64

# 可能存在的问题：
max2 = functools.partial(max, 10)
print max2(5,6,7)
# 10
# 上面相当于args=(10,5,6,7)
# max(*args)