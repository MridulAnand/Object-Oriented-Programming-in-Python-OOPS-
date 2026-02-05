# access specifiers: public private protected
class A:
    def __init__(self):
        self.name = "Abc" # public
        # it can be accessed in sub classes of A
a = A()
print(a.name)

class A:
    def __init__(self):
        self._name = "Abc" # protected
        # it can be accessed in sub classes of A
a = A()
print(a._name) # Can be accessed but not recommended and discouraged it should only be used inside class

class A:
    def __init__(self):
        self.__name = "Abc" # private
        # it can be accessed in sub classes but not directly, we need to do name mangling (example self._A__name)
a = A()
# print(a.__name) #not correct way to call
print(a._A__name) # name mangling is done to access it means we need to suffix class name

class A:
    def aa(self): # public method
        print("Aa")
        
    def _bb(self): # protected method
        print("Bb")
        
    def __cc(self): # private method
        print("Cc")

a = A()
a.aa()
a._bb() # not recommended
#a.__cc() # not correct way to call
a._A__cc()

#in python we can't specify access for classes so we can use __all__ to control the access of classes