# -*-:coding:utf-8 -*-
# 继承 多态

class Animal(object):
	def run(self):
		print 'Animal is running...'

	def eat(self):
		print 'I can eat.'

class Dog(Animal):
	# override the super method
	def run(self):
		print 'Dog is running...'

	# call the super method
	def openYourMouth(self):
		return super(Dog, self).eat()

class Cat(Animal):
	def run(self):
		print 'Cat is running...'

def run(animal):
	animal.run()

run(Animal())
run(Dog())
run(Cat())

Dog().openYourMouth()