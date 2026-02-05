# method overloading in python
class A:
    def method(self,name,age = None,height = None):    # this way is used for method overloading in python but it has limited parameters to have many parameters we can use *args and **kwargs
        print(name, age if age else "", height if height else "")
        
a = A()
a.method("Abc")

aa = A()
aa.method("Abc",20)

aaa = A()
aaa.method("Abc",20,175)

# Method overloading using *args and **kwargs it can take any number of parameters
class A:
    def method(self,*args,**kwargs):   
        # *args → tuple of positional arguments
        # **kwargs → dictionary of keyword arguments 
        print(args) # positional arguments
        print(kwargs) #keyword arguments
        
a = A()
a.method("Abc")
print()

aa = A()
aa.method("Abc",age=20)
print()

aaa = A()
aaa.method(name="Abc",age=20,height=175)