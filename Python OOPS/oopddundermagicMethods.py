# example of using magic/dunder (double underscore) methods to customize behavior of operators in a class
class A:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __add__(self,other):
        return A(self.x+other.x,self.y+other.y)
        
    def __mul__(self,other):
        # return A(self.x*other.x,self.y*other.y) # coordinate wise multiplication
        return self.x*other.x+self.y*other.y # dot product
        
    def __repr__(self):
        return f"{self.x,self.y}"
        
a = A(1,2)
b = A(3,4)
c = a+b
d = a*b
print(f"{a}+{b}={c}\n{a}*{b}={d}")  # example of Vector using customized add and multiply
# these are examples of operator overloading using dunder methods in python and these are some of many dunder methods available in python to customize behavior of operators and built-in functions for user-defined classes.
# Some commonly used dunder methods: - __init__, __del__, __str__, __repr__, __eq__, __add__, __len__, __getitem__, __iter__
# We can define more dunder methods to customize behavior of other operators and built-in functions as per our requirements. To know more about dunder methods we can refer to python documentation.