class A:
    def __init__(self,name):
        self.name = name
        print(f"constructor called for {self.name}")
    def __del__(self):
        print(f"deleted {self.name}")
    def printer(self):
        print(self.name)
a = A("Abc")
a.printer()
del(a) # or del a
# printer() # it will give error  name 'a' is not defined