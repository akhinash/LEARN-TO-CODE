def upperdec(func):
    def wrapper(x):
        result = func(x)
        return result.upper()
    return wrapper

@upperdec
def say_hello(n):
    return f"Hello {n}"

print(say_hello("Alice"))