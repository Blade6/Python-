# -*- coding:utf-8 -*-
#字符串和文本
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# %r会显示变量的原始数据，即x是字符串，输出的时候会体现出来。
# raw representation,%r 适用于debug(调试)
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#把一个字符串放进另一个字符串
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

#字符串相连
print w+e

#打印10个点
print "." * 10 

#三引号(可以直接写换行的字符串，而不用做处理。)
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print fat_cat

text = "this hack is wack hack"
lis = text.split()
# ['this', 'hack', 'is', 'wack', 'hack']