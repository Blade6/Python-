# encoding:utf-8
# 函数作为返回值
# 闭包（Closure）是词法闭包（Lexical Closure）的简称，是引用了自由变量的函数。
# 这个被引用的自由变量将和这个函数一同存在，即使已经离开了创造它的环境也不例外。
# 所以，有另一种说法认为闭包是由函数和与其相关的引用环境组合而成的实体。
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
# 我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
# 调用lazy_sum()时，返回的不是求和结果，而是求和函数
f = lazy_sum(1,3,5,7,9)
print f
# <function sum at 0x10452f668>
# 调用函数f时，才去计算求和的结果
print f()
# 25
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print f1==f2
# False
# 当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
# f1()和f2()的调用结果互不影响

# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs

# f1, f2, f3 = count()
# 表面上看f1(),f2(),f3()将分别得到1,4,9
# 实际上都是9
# 理由:fs中记录了3个f函数，每个f函数包括它本身的函数体和变量i的内存地址
# f1()执行时，去变量i的内存地址取值，发现它的值不再是1，变成3了

# 因此，返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

def count():
    fs = []
    for i in range(1, 4):
        def f(j=i):
             return j*j
        fs.append(f)
    return fs
f1, f2, f3 = count()
print f1(),f2(),f3()
# 1 4 9
# j绑定了当前的i的值，每个f的j都是私有的，不同的