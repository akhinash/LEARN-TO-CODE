def multi(func):
    def wrapper(a, b):
        return func(a, b) * 2
    return wrapper      

@multi
def multiply(x, y):
    return x * y                
print(multiply(3, 4))
