import math


#class Shape:
#	def __init__(self):
#		raise NotImplementedError()
#
#	def GetArea(self): pass
#	def GetPerimeter(self): pass


#Cuboid Definition (rectangular prism)
class Cuboid:
    def __init__(self, width:float, height:float, depth:float) -> None:
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self): 
        return (self.width * 2) + (self.height * 2)

#Cube Definition (child of cuboid)
class Cube:
    def __init__(self, width:float, height:float, depth:float) -> None:
        self.width = width
        self.height = height
  
    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return (self.width * 2) + (self.height * 2)

#Cylinder Definition
class Cylinder:
    def __init__(self, radius) -> None:
        self.radius = radius

    def getArea(self):
        return math.pi * (self.radius ** 2)

    def getPerimeter(self):
        return 2 * math.pi * self.radius ** 2


class Polygon:
	def __init__(self, sideLength:float, sides:int):
		''' A representation of a regular polygon defined by sides and side length.

		Maths functions will be pulled from the wiki page:
		https://en.wikipedia.org/wiki/Regular_polygon

		Arguments:
			sideLength(float): The length of the sides. Regular polygons have congruent side lengths. Must be a positive, non-zero number.
			sides(int): The number of sides that the regular polygon will have. Must be a number larger than 2.
		'''
		# Validating side length
		if sideLength <= 0:
			raise ValueError(f'sideLength must by a positive, non-zero number. Received `{sideLength}`.')

		# Validating side count
		if sides < 3:
			raise ValueError(f'side count must be a number larger than 2. Received `{sides}`')

		# Setting member variables now that we've validated input
		self._sideLength = sideLength
		self._sides = sides

	def GetArea(self) -> float:
		''' Gets the area of the regular polygon.

		Returns: A float representing the area of the regular polygon.
		'''
		cotComponent = (
			math.cos(math.pi / self._sides)
			/
			math.sin(math.pi / self._sides)
		)

		return (self._sides / 4) * cotComponent

	def GetPerimeter(self) -> float:
		''' Gets the perimeter of the regular polygon.

		Returns: A float representing the perimeter of the regular polygon.
		'''
		return self._sideLength * self._sides