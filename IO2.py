# -*- coding:utf-8 -*-
# 读写文件
# close--保存并关闭文件
# read--读取文件内容
# readline--读取文本文件的一行
# truncate--清空文件
# write(stuff)--将stuff写入文件

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename,'w')
#以写入模式打开，还有r只读模式，a追加模式(append)

print "Truncating the file. Goodbye!"
target.truncate()
#truncate()是截取函数

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()