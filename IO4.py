# -*- coding:utf-8 -*-
#函数与文件

from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

# seek(0)转到文件的0 byte也就是第一个字节的位置	
def rewind(f):
	f.seek(0)

# readline()会扫描文件的每一个字节，直到找到一个\n为止
# readline()返回的内容中包含文件本来就有的\n	
# 文件f会记录位置，这样下次调用就会读取下一行
def print_a_line(line_count, f):
	print line_count, f.readline()
	
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)