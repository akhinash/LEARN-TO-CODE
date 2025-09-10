def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
from itertools import count


def find_area(l,b):
    area=l*b
    return area

a=find_area(6,4)
print(a)

def my_function():
    x=10
    print("local variable:",x)
my_function()


pi=3.14
def find_area(r):
    area=pi*r*r
    return area
a=find_area(5)
print(a)

v=100
def  demo():
    v=10
    print(v)
demo()
print(v)


count=0
def abcd():
    global count
    count=count+1
    print("hi")
    print(f"this function called {count} times")
abcd()
abcd()
abcd()