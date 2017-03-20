#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-02 19:59:34
# @Author  : Blade6:blouisloveyou@gmail.com

from multiprocessing import Process
import os

def run_proc(name):
	print 'Run child process %s (%s)...' % (name, os.getpid())

if __name__ == '__main__':
	print 'Parent process %s.' % os.getpid()
	p = Process(target=run_proc, args=('test',))
	print 'Process will start.'
	p.start()
	p.join()
	# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
	print 'Process end.'	