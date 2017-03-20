#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-02 20:06:26
# @Author  : Blade6:blouisloveyou@gmail.com

# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程
from multiprocessing import Pool
import os, time, random

def long_time_tast(name):
	print 'Run task %s (%s)...' % (name, os.getpid())
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print 'Task %s runs %0.2f seconds.' % (name, (end - start))

if __name__ == '__main__':
	print 'Parent process %s.' % os.getpid()
	p = Pool()
	for i in range(5):
		p.apply_async(long_time_tast, args=(i,))	
	print 'Waiting for all subprocesses done...'
	p.close()
	p.join()
	print 'All subprocesses done.'

# 对Pool对象调用 join()方法会等待所有子进程执行完毕，调用 join()之前必须先调用 close()，调用 close()之后就不能继续添加新的Process了	

# Parent process 2788.
# Waiting for all subprocesses done...
# Run task 0 (1912)...
# Task 0 runs 1.39 seconds.
# Run task 1 (15388)...
# Task 1 runs 1.92 seconds.
# Run task 3 (16236)...
# Task 3 runs 2.48 seconds.
# Run task 2 (12296)...
# Task 2 runs 1.17 seconds.
# Run task 4 (12296)...
# Task 4 runs 1.66 seconds.
# All subprocesses done.

# 请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。如果改成：
# p = Pool(5)
# 就可以同时跑5个进程。
# 由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果。