# -*- coding:utf-8 -*-
import os

# 更改工作目录
os.chdir('D:\\DSST_code\\code\\sequences\\David\\img')

# 打印工作目录
# print(os.getcwd())

for x in range(771):
	if x == 0:
		continue
	else:
		if x < 10:
			oldname = "000%d.jpg" % x
			newname = "img0000%d.jpg" % x
		elif x < 100:
			oldname = "00%d.jpg" % x
			newname = "img000%d.jpg" % x
		else:
			oldname = "0%d.jpg" % x
			newname = "img00%d.jpg" % x
		os.rename(oldname,newname)
		
		

