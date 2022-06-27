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