#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-02 20:19:17
# @Author  : Blade6:blouisloveyou@gmail.com

# 进程间通信
# inter-process communication

# 除了Queue，还可以使用Pipes
from multiprocessing import Process, Queue
import os, time, random

# 写数据
def write(q):
	for value in ['A', 'B', 'C']:
		print 'Put %s to queue...' % value
		q.put(value)
		time.sleep(random.random())

# 读数据
def read(q):
	while True:
		value = q.get(True)
		print 'Get %s from queue.' % value

if __name__ == '__main__':
	# 父进程创建Queue，并传给各个子进程
	q = Queue()		
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))
	# 启动子进程pw，写入
	pw.start()
	# 启动子进程pr，读入
	pr.start()
	# 等待pw结束
	pw.join()
	# pr进程里是死循环，无法等待其结束，只能强行终止
	pr.terminate()

# 在Unix/Linux下，multiprocessing模块封装了 fork()调用，使我们不需要关注 fork()的细节。
# 由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，
# 父进程所有Python对象都必须通过pickle序列化再传到子进程去，所以，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。