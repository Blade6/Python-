# -*- coding:utf-8 -*-
from sys import argv
#导入sys模块
#如果参数是在用户执行命令时就要输入，就是argv，如果是在脚本运行过程中输入，那就是用raw_input()

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:",third