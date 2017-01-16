# encoding:utf-8
# hello.py
"""
Here you can write multi line comment
"""

classmates = ['Bob','David','Nancy']
print classmates
# ['Bob','David','Nancy']

print classmates[0]
# 'Bob'

david_index = classmates.index("David")
# david_index = 1

print classmates[-1]
# 'Nancy'
# -1 means the last one,-2 means the one before last one,but you can beyond the range
# so you can get classmates[-4]

classmates.insert(1,'Jack')
print classmates
# ['Bob','Jack',David','Nancy']

classmates.append('Adam')
print classmates
# ['Bob','Jack',David','Nancy','Adam']

classmates.remove('Jack')
# classmates.pop()
# ['Bob','Jack',David','Nancy']
# default pop the last one

classmates.pop(1)
# ['Bob','David','Nancy']

L = ['Apple', 123, True, ['asp', 'php']]
# the element of list can be different,even list
print L[3][1]
# php

L = []
# an empty list

