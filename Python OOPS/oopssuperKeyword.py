# Use of super keyword and method overriding in OOPS in python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,l,b):
        self.l = l
        self.b = b
    @property    
    def area(self): # Overriding area method of Shape class
        return f"Rectangle: {self.l*self.b}"

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side) # Super Keyword to call parent class constructor
    @property    
    def area(self):
        return f"Square: {self.l*self.b}"
        
class Cube(Square):
    def __init__(self,side):
        Square.__init__(self,side) # Calling parent class constructor without super keyword but not recommended in case of multiple and complex inheritance
    @property    
    def area(self):
        return f"Cube: {6*self.l*self.l}"

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    @property    
    def area(self):
        return f"Circle: {self.radius*self.radius*3.14}"
        
a = Rectangle(1,2)
print(a.area)

b = Square(2)
print(b.area)

c = Cube(2)
print(c.area)

d = Circle(1)
print(d.area)
        
