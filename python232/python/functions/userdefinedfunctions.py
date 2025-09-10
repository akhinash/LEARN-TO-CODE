# def add(x,y):
#     result=x+y
#     return result
# print(add(2,6))


# def name(a):
#     print("hello",a)
# name("akhinash")
#
# #type of arguments
#1 positional arguments

# def total(a,b,c,d):
#     area=a+b+c+d
#     return area
# print(total(22,44,77,88))

# def person(name,age,salary,place):
#     newsal=salary*2
#     return newsal
# print(person(name='akhi',salary=300000,age=24,place='kochi'))

# def sum(a,b,c=9):
#     a=a+b+c
#     return a
# print(sum(1,2))
#
#
# def sum(a,b,c=9):
#     a=a+b+c
#     return a
# print(sum(1,2,3))

def find(*a):
    print("hi")
    return
find(1,2,3)

def details(*a):
    for i in a:
        print(i)
details('achu',22,"nichu")
