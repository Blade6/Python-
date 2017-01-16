# -*- coding:utf-8 -*-
# 读取文件
from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

#Python不会限制你打开文件的次数，事实上，有时候多次打开同一个文件是一件必须的事情