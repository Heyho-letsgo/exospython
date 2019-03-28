# coding: utf-8

class Person:
	def __init__(self,name,age, comm):
		self.name = name
		self.age = age
		self.comm = comm
		

	def myfunc(self):
		print(self.comm, "Hello mon nom est ", self.name, "et j'ai ", self.age)


p1 = Person("John",36,"kqhsdjkqshdjkhqjk"	)
p2 = Person("Andy",26, "oduyaiuyoauouzeaop")

p1.age = 128
del p1.age
p1.age = 128

del p1

try:
	p1.myfunc()
except NameError: 
	p2.myfunc()
else:
	p1.myfunc()
	p2.myfunc()

