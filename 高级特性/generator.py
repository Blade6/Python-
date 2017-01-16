# encoding:utf-8
# 生成器
# 列表生成式虽然可以生成列表，但是如果列表很大的话，就很占内存
# 生成器保存推算规则，要用的时候再推算出来，从而节省大量的空间

# 与列表生成式相似，只是最外面变成小括号
g = (x * x for x in range(10))
print g.next()
# 0
print g.next()
# 1
print g.next()
# 4
print g.next()
# 9
print g.next()
# 16
print g.next()
# 25
print g.next()
# 36
print g.next()
# 49
print g.next()
# 64
print g.next()
# 81
# print g.next()
# 报错

g = (x * x for x in range(10))
for n in g:
	print n
# 我们创建了一个generator后，基本上永远不会调用next()方法，而是通过for循环来迭代它。

# 斐波拉契数列
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1

# 把这个函数改成生成器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
# print fib(6)
# <generator object fib at 0x104feaaa0>
# 0x104feaaa0 是本次运行所在内存位置，每次运行不同。
for n in fib(6):
	print n

def odd():
	print 'step 1'
	yield 1
	print 'step 2'
	yield 3
	print 'step 3'
	yield 5

o = odd()
print o.next()
print o.next()
print o.next()

print o.next()
# 出错，odd()是生成器，执行过程中遇到yield就中断，下一次调用odd()会从上次中断的地方继续执行
# odd()函数的yield次数是有限的，3次，所以执行3次后已经没有yield了，第4次调用就会出错

# 对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。