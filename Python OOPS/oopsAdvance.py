from abc import ABC, abstractmethod 
# Abstract Base Class (ABC) is a class that cannot be instantiated and is designed to be subclassed. It can contain abstract methods, which are methods that are declared but not implemented in the base class. Subclasses of the ABC must implement the abstract methods in order to be instantiated.
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return self.radius*self.radius*3.14

a = Circle(1)
print(a.area())

# Mixins, - A mixin is a small class that provides additional functionality when combined with other classes. They are not meant to stand alone — only to “mix in” behavior.

class LoggerMixin:
    def log(self,message):
        print("[Log]:",message)

class Service(LoggerMixin):
    def process(self):
        self.log("Processing Started")
       
aa = Service()
aa.process()

# Meta classes, - A metaclass is a class of a class that defines how a class behaves. A class is an instance of a metaclass. The most common use of metaclasses is to create classes that have certain properties or behaviors, such as automatically registering subclasses or enforcing certain naming conventions.

class Meta(type):
    def __new__(cls,name,bases,dct):
        print("Creating class",name)
        return super().__new__(cls,name,bases,dct)

class MyClass(metaclass=Meta):
    pass

MyClass()

# Encapsulation with properties - Encapsulation is the concept of hiding the internal state and behavior of an object and only exposing a public interface. In Python, we can achieve encapsulation using properties, which allow us to define getter and setter methods for an attribute.

class Person:
    def __init__(self,name):
        self._name = name #protected attribute
    
    @property  #getter method 
    def name(self):
        return self._name
    
    @name.setter  #setter method
    def name(self,value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

aaa = Person("Abc")
print(aaa.name)
aaa.name = "Acb"
print(aaa.name)
# aaa.name = "" #ValueError will be 

# Class method - A class method is a method that is bound to the class and not the instance of the class. It can access and modify class state that applies across all instances of the class. Class methods are defined using the @classmethod decorator.

class Person1:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def printer(self):
        print("Name:",self.name,"Age:",self.age)
    @classmethod
    def classmethod1(cls,name_age_list):
        name = name_age_list[0]
        age = name_age_list[1]
        return cls(name,age)

a1 = Person1("Abc",20)
a1.printer()
a1 = Person1.classmethod1(["Acb",22])
a1.printer()