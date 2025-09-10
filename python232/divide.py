def div(func):
    def wrapper(a, b):
        if b == 0:
            return "Division by zero error"
        else:
            return func(a, b)
    return wrapper

@div
def divide(x, y):
    return (x / y)

print(divide(10, 2))
print(divide(10, 0))