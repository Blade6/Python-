#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-18 20:14:04
# @Author  : Blade6:blouisloveyou@gmail.com

import os

mylist = os.listdir(os.getcwd())
for item in mylist:
	if os.path.isfile(item):
		if '.bak' in item:
			os.remove(item)

print 'Done!'