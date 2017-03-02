# -*- coding:utf-8 =*-

# 自定义错误，建议尽量用python内置的错误
# class FooError(StandardError):
# 	pass

# def foo(s):
# 	n = int(s)
# 	if n==0:
# 		raise FooError('invalid value: %s' % s)
# 	return 10 / n

# foo('0')

def foo(s):
	n = int(s)
	return 10 / n

def bar(s):
	try:
		return foo(s) * 2
	except StandardError, e:
		print 'Error'
		raise

# 捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。
# raise语句如果不带参数，就会把当前错误原样抛出。

def main():
	bar('0')

main()