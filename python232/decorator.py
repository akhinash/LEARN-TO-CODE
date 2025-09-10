def dec(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
        
    return wrapper
@dec
def say_hello():
    print("Hello!") 
say_hello()
