import math
def areacirc(func):
    def wrapper(x):
        area = func(x)
        if x < 0:
            return "Radius cannot be negative"
        else:
            return f"Area of circle: {area}"
    return wrapper

@areacirc
def area(r):
    return math.pi * r * r         
print(area(5))
print(area(-3))