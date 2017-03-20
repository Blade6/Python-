#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-17 19:21:11
# @Author  : Blade6:blouisloveyou@gmail.com

import requests

r = requests.get('http://cstfs.gdufs.edu.cn/')

print(r.text)