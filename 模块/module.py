#!/usr/bin/env python
# -*- coding:utf-8 -*-

'a test module'

__author__ = 'Blade6'

import sys

def test():
	args = sys.argv
	if len(args)==1:
		print 'Hello World'
	elif len(args)==2:
		print 'Hello, %s' % args[1]
	else:
		print 'Too many arguments!'

if __name__=='__main__':
	test()

# 在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__
# 在其他地方运行需要调用hello.test()才会显示

# try:
#     import cStringIO as StringIO
# except ImportError: # 导入失败会捕获到ImportError
#     import StringIO
# Python标准库一般会提供StringIO和cStringIO两个库，这两个库的接口和功能是一样的，但是cStringIO是C写的，速度更快
# 这样就可以优先导入cStringIO。如果有些平台不提供cStringIO，还可以降级使用StringIO。导入cStringIO时，用import ... as ...指定了别名StringIO，因此，后续代码引用StringIO即可正常工作

# try:
#     import json # python >= 2.6
# except ImportError:
#     import simplejson as json # python <= 2.5
# 类似simplejson这样的库，在Python 2.6之前是独立的第三方库，从2.6开始内置

# 由于Python是动态语言，函数签名一致接口就一样，因此，无论导入哪个模块后续代码都能正常工作


# 作用域
# 在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
# 我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，这样，调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：
# 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public