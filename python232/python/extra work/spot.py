# num1=int(input("enter the first number"))
# num2=int(input("enter the second number"))
# op=input("select operation( add, mul, div, sub)")
# if op == 'add':
#     print("Result:", num1 + num2)
# elif op == 'sub':
#     print("Result:", num1 - num2)
# elif op == 'mul':
#     print("Result:", num1 * num2)
# elif op == 'div':
#     if num2 != 0:
#         print("Result:", num1 / num2)
#     else:
#         print("Error! Division by zero.")
# else:
#     print("Invalid operation!")

#
# a=[2,6,4,8,9]
# a.sort()
# print(a[-2])

# size = int(input("enter sixe"))
# for row in range(1, size):
#     for sp in range(1, size - row):
#         print(" ", end="")
#     for col in range(1, row + 1):
#         print("* ", end="")
#
#     print()

a="*"
b=1
c=int(input('enter size'))
while b<=c:
    print(a*b)
    b=b+1
