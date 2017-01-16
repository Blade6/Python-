# -*-:coding:utf-8 -*-
# 继承 多态

class Animal(object):
	def run(self):
		print 'Animal is running...'

class Dog(Animal):
	def run(self):
		print 'Dog is running...'

class Cat(Animal):
	def run(self):
		print 'Cat is running...'

def run(animal):
	animal.run()

run(Animal())
run(Dog())
run(Cat())