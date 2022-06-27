#!/usr/bin/python3
'''An empty class Rectangle that defines a rectangle'''

class Rectangle:
	'''Class tha represent a Rectangle'''
	number_of_instances = 0
	print_symbol = "#"


	__init__(self, width = 0, height = 0):
		''' '''
		self.__width = width
		self.__height = height
		number_of_instances += 1

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
				representation = representation + self.print_symbol
			representation = representation + "\n"
		return representation

	def __repr__(self):
	'''Methode print Rectangle with #
	Return: representation'''
		representation = Rectangle()
		if self.__height <= 0 or self.__width <= 0:
			representation = self
		return representation

	def __del__(self):
	'''Methode delete Rectangle'''
		try:
			number_of_instances -= 1
			print("Bye rectangle...")
		except Exception:
			print("No instance of Rectangle")

	@staticmethod
	def bigger_or_equal(rect_1, rect_2):
		''' 
		Return the biggest rectangle
		Return: Rectangle
		'''
		if not isinstance(rect_1, Rectangle):
			raise TypeError("rect_1 must be an instance of Rectangle")
		elif not isinstance(rect_2, Rectangle):
			raise TypeError("rect_2 must be an instance of Rectangle")
		else:
			if rect_1.area() == rect_2.area():
				print(rect_1)
			elif rect_1.area < rect_2.area:
				print (rect_2)
			else:
				print(rect_1)


		