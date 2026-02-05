# Single Inheritance Example

class A:
    def car_name(self):
        print("Tata Nexon")

class B(A):
    def car_colour(self):
        print("Car colour is white")

a = B()
a.car_name()
a.car_colour()

print()

# Multilevel Inheritance Example

class A:
    def car_name(self):
        print("Tata Nexon")

class B(A):
    def car_colour(self):
        print("Car colour is white")

class C(B):
    def car_model(self):
        print("Car model is 2024")

a = C()
a.car_name()
a.car_colour()
a.car_model()

print()

# Multiple Inheritance Example with Method Resolution Order (MRO)

class A:
    def move(self):
        print("Vehicle can move")

class B(A):
    def drive(self):
        print("Car drives on road")
    def sail(self):
        print("Car can't sail on water")

class C(A):
    def drive(self):
        print("Boat cant't drive on road")
    def sail(self):
        print("Boat sails on water")

class D(B,C):
    def special(self):
        print("AmphibiousCar can drive and sail")

class E(C,B):
    def special(self):
        print("AmphibiousCar can drive and sail")
        
a = D()
a.move()
a.drive()
a.sail()
a.special()
print(D.mro()) # checking MRO (Method resolution order)

print()

a = E()
a.move()
a.drive()
a.sail()
a.special()
print(E.mro()) # checking MRO (Method resolution order)

print()

# Hierarchical Inheritance Example

class A:
    def car_name(self):
        print("Tata Nexon")

class B(A):
    def car_colour(self):
        print("Car colour is white")

class C(A):
    def car_colour(self):
        print("Car colour is gray")

a = B()
a.car_name()
a.car_colour()

print()

b = C()
b.car_name()
b.car_colour()

print()

# Hybrid Inheritance Example

class A:
    def car_name(self):
        print("Tata Nexon")

class B:
    def car_feature(self):
        print("Car has sunroof")

class C(A):
    def car_colour(self):
        print("Car colour is white")

class D(A,B):
    def car_colour(self):
        print("Car colour is gray")

a = C()
a.car_name()
a.car_colour()

print()

b = D()
b.car_name()
b.car_colour()
b.car_feature()
