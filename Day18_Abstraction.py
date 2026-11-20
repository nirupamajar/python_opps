#Abstraction means hiding complex logic and showing only the necessary information/parts. Abstract class and abstract methods

from abc import ABC, abstractmethod
from math import pi
class shape(ABC): #parent class

    @abstractmethod
    def area(self):
        pass

class rectangle(shape): #child class 1
    def __init__(self, length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        areaofrec = self.length * self.breadth
        return areaofrec

class circle(shape): # child class 2
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        areaofcir = pi * (self.radius **2)
        return areaofcir

length = int(input("Enter the length of the rectangle:"))
breadth = int(input("Enter the breadth of the rectangle:"))
rectangleobj = rectangle(length,breadth)
print("Area of the rectangle is : ",rectangleobj.area())

radius = int(input("Enter the radius of the circle: "))
circleobj = circle(radius)
print("Area of the circle is : ",circleobj.area())

