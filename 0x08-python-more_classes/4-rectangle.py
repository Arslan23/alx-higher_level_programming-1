#!/usr/bin/python3
'''An empty class Rectangle that defines a rectangle'''

class Rectangle:
	'''Class tha represent a Rectangle'''
	__init__(self, width = 0, height = 0):
		''' '''
		self.__width = width
		self.__height = height

	@property
	def width(self):
		'''Get width'''
		return self.__width

	@width.setter
	def width(self, value):
		'''Set width'''
		try:
			if isinsert(value,int):
				if value <= 0:
					raise ValueError("width must be >= 0")
				else:
					self.__width = value
			else:
				raise TypeError("width must be an integer")

	@property
	def height(self):
		'''Get height'''
		return self.__width

	@height.setter
	def height(self, value):
		'''Set height'''
		try:
			if isinsert(value,int):
				if value <= 0:
					raise ValueError("height must be >= 0")
				else:
					self.__height = value
			else:
				raise TypeError("height must be an integer")
	def area(self):
		'''Public methode area that return the rectangle area
		Return : height * width
		'''
		return self.__height * self.__width

	def perimeter(self):
		'''Public methode perimeter that return the rectangle perimeter
		Return : 0 if height or width less equal 0 , else perimeter
		'''
		if self.__height <= 0 or self.__width <= 0:
			return 0
		else:
			return (self.__height + self.__width) * 2

	def __str__(self):
	'''Methode print Rectangle with #
	Return: representation'''
		representation = ""
		if f self.__height <= 0 or self.__width <= 0:
			return representation
		for i in range(1,self.__height + 1):
			for j in range (1,self.__width + 1):
				representation = representation + "#"
			representation = representation + "\n"
		return representation

	def __repr__(self):
	'''Methode print Rectangle with #
	Return: representation'''
		representation = ""
		if f self.__height <= 0 or self.__width <= 0:
			return representation
		for i in range(1,self.__height + 1):
			for j in range (1,self.__width + 1):
				representation = representation + "#"
			representation = representation + "\n"
		return representation