#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-17 18:21:21
# @Author  : Blade6:blouisloveyou@gmail.com

import requests

KEY = '71f28bf79c820df10d39b4074345ef8c'

def getResponse(msg):
	apiUrl = 'http://www.tuling123.com/openapi/api'
	data = {
		'key'     : KEY,
		'info'    : msg,
		'userid'  : 'wechat-robot',
	}
	try:
		r = requests.post(apiUrl, data=data).json()
	except:
		return "Error!"
	return r.get('text')

f = open('chatLog.txt','a')

while(True):
	msg = input('> ')
	if msg == 'exit':
		break
	ans = getResponse(msg)
	if ans == 'Error!':
		print(ans)
		break
	if u'\xa0' in ans:
		ans = ans.replace(u'\xa0',' ')
	try:
		f.write("> "+msg+"\n: "+ans+"\n")
	except:
		print('ans is ilegal')
		break
	print(":", ans)

f.close()