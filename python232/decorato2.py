def dec(func):
    def wrapper(x):
        print("Before function call")
        func(x)
        print("After function call")
    return wrapper

@dec
def say_hello(n):
    print("Hello!",n)                 
say_hello("AKSH")