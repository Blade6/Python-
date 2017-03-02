# - *- coding:utf-8 -*-
# 多重继承

class Animal(object):
	pass

class Mammal(Animal):
	pass

class Bird(Animal):
	pass

class Runnable(object):
	def run(self):
		print('Running...')

class Flyable(object):
	def fly(self):
		print('Flying...')

class Dog(Mammal, Runnable):
	pass

class Bat(Mammal, Flyable):
	pass

# 为了解决多重继承的问题，Java引入了接口 （interface）技术，Lisp、Ruby引入了 Mix-in 技术。
# 以 Ruby 为例，Mix-in 有效地降低多重继承复杂性（谁是你爹，哪个爹的优先级高，你的把妹方法是继承自哪个爹的等）。 Ruby中 Mix-in 的单位是 模块 （module）。
# Mix-in 技术按一下规则来限制多重继承：
# 继承用但一继承；
# 第二个及两个以上的父类必须是 Mix-in 的抽象类。

# Mix-in 类是具有以下特征的抽象类：
# 不能单独生成实例；
# 不能继承普通类。

# 按照以上的原则，类在层次上具有单一继承一样的树结构，同时又可以实现功能的共享（方法是：把共享的功能放在 Mix-in 类中，再把 Mix-in 类插入到树结构里）。

# Java 用 接口 解决规格继承（类都有哪些方法）的问题，Mix-in 则解决了实现继承（类中都用了什么数据结构和什么算法）的问题。