#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-02 19:23:59
# @Author  : Blade6:blouisloveyou@gmail.com

import json

class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age 
		self.score = score

s = Student('Bob', 20, 88)

# 方法一
def student2dict(std):
	return {
		'name': std.name,
		'age': std.age,
		'score': std.score
	}

print(json.dumps(s, default=student2dict))

# 方法二
print(json.dumps(s, default=lambda obj: obj.__dict__))
# 通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class

# 如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))