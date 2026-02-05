# A simple decorator that prints messages before and after the execution of a function. It works with both type functions whether they need arguments or not
def decorator1(func):
    def wrapper(*args,**kwargs):
        print("Welcome")
        result = func(*args,**kwargs)
        print("Thank you")
        return result
    return wrapper

@decorator1 # This is equivalent to a = decorator1(aa) and one of the way to apply decorator
def a(a):
    print(a)
a("Hello")

def aa(a):
    print(a)

a = decorator1(aa) # Another way to apply decorator, both ways work similarly
a("hello")

# A decorator that prints messages before and after the execution of a function and also prints the return value of the function. It works with both type functions whether they need arguments or not but it should be of return type 
def decorator2(func):
    def wrapper(*args,**kwargs):
        print("Welcome")
        result = func(*args,**kwargs)
        print(result)
        print("Thank you")
        return result
    return wrapper

@decorator2
def a(a):
    return a
a("Hello")

# It works same as above but with a check for None return type, so it works with both type functions whether they need arguments or not and whether they are of return type or not
def decorator3(func):
    def wrapper(*args,**kwargs):
        print("Welcome")
        result = func(*args,**kwargs)
        if result is not None:
            print(result)
        print("Thank you")
        return result
    return wrapper

@decorator3
def a(a):
    return a
a("Hello")

@decorator3
def aa(a):
    print(a)
a("Hello")

# A simple decorator that prints messages before and after the execution of a function. It only works with functions that do not need arguments
def decorator4(func):
    def wrapper():
        print("Welcome")
        result = func()
        print("Thank you")
        return result
    return wrapper

@decorator4
def a():
    print("Hello")
a()

# A simple decorator that prints messages before and after the execution of a function. It only works with functions that need one argument ,we can increase the number of arguments as per requirement
def decorator5(func):
    def wrapper(a):
        print("Welcome")
        result = func(a)
        print("Thank you")
        return result
    return wrapper

@decorator5
def aa(a1):
    print(a1)
aa("Hello")

# A decorator that measures the execution time of a function. It works with both type functions whether they need arguments or not
import time

def decorator6(func):
    def wrapper(*args,**kwargs):
        a = time.time()
        result = func(*args,**kwargs)
        b = time.time()
        print(f"{b-a:.10f}")
        return result
    return wrapper
    
@decorator6
def a():
    print("Run Time")
    print("Hello")
a()

# A decorator factory that takes an argument n and returns a decorator that runs the decorated function n times. It works with both type functions whether they need arguments or not
def decorator8(n):
    def decorator7(func):
        def wrapper(*args,**kwargs):
            for i in range(n):
                func(*args,**kwargs)
        return wrapper
    return decorator7

@decorator8(6)
def a():
    print("Hello")
a()