#Task1
from math import pi


class Circle:
	
	def __init__(self, radius):
		self.radius = radius


	def area(self):
		self.area_ = self.radius ** 2 * pi
		print("The area of circle is", self.area_)

	def perimeter(self):
		self.perimeter_ = 2 * pi * self.radius
		print("The perimeter of circle is", self.perimeter_)


#Task2


#Task3

class Person:
	
	def __init__(self, gender):
		self.gender = gender

class Student(Person):
	
	def __init__(self, gender, name, surname, age, profession, group):
		Person.__init__(self, gender)
		self.name = name
		self.surname = surname
		self.age = age
		self.profession = profession
		self.group = group




