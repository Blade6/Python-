#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-02 19:19:22
# @Author  : Blade6:blouisloveyou@gmail.com

import json
d = dict(name='Bob', age=20, score=88)
print json.dumps(d)
# {"age": 20, "score": 88, "name": "Bob"}

# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
# 要把JSON反序列化为Python对象，用 loads()或者对应的 load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化
# >>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# >>> json.loads(json_str)
# {u'age': 20, u'score': 88, u'name': u'Bob'}
# 有一点需要注意，就是反序列化得到的所有字符串对象默认都是unicode而不是str。由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str或unicode与JSON的字符串之间转换。