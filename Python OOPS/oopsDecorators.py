from abc import ABC,abstractmethod
from dataclasses import dataclass

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle():
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return self.radius**2*3.14

@dataclass
class DC:
    radius:float
    def area(self):
        return self.radius**2*3.14
        
class A:
    def __init__(self,radius):
        self.radius = radius
    def area1(self):
        return self.radius**2*3.14
    @property
    def area(self):
        return self.radius**2*3.14
    @classmethod
    def classmethod(cls,diameter):
        radius = diameter
        return cls(radius)
    
class B:
    @staticmethod
    def staticfunction(radius):
        return radius**2*3.14
        
class GS:
    def __init__(self,radius):
        self.radius = radius
    @property
    def area(self):
        return self.radius**2*3.14
    @area.setter
    def area(self,value):
        self.radius = value
        
a = A(1)
print(a.area1())
print(a.area)
a1 = A.classmethod(1)
print(a1.area1())

#a2 = Shape() #TypeError: Can't instantiate abstract class Shape without an implementation for abstract method 'area'
a2 = Circle(1)
print(a2.area())

a3 = DC(1)
print(a3.area())
print(a3) # __repr__

a4 = DC(1)
print(a4.area())
print(a4)

print(a3 == a4) # __eq__

print(B.staticfunction(1))

a5 = GS(1)
print(a5.area)
a5.area = 2
print(a5.area)