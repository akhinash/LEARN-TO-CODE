#qn1
# name=input("enter your name")
# age=int(input("enter your age"))
# print("Hello,",name,"!tou are",age," yaers old")


#qn2
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# operation = input("select operation (add,sub,mul,div): ")
#if operation == 'add':
#     print("Result:", num1 + num2)
# elif operation == 'sub':
#     print("Result:", num1 - num2)
# elif operation == 'mul':
#     print("Result:", num1 * num2)
# elif operation == 'div':
#     if num2 != 0:
#         print("Result:", num1 / num2)
#     else:
#         print("Error! Division by zero.")
# else:
#     print("Invalid operation!")


#qn3

# year=int(input("enter a year"))
# if year%4==0:
#     print("leap year")
# else:
#     print(("not leap year"))

# #qn4
#
# age=int(input("enter your age"))
# if age>=18:
#     print("elgible to vote")
# else:
#     print("not elgible")

# #qn5
# a=int(input("enter length of first side"))
# b=int(input("enter the length of sec side"))
# c=int(input("enter the length of 3rd side"))
# if a==b==c:
#     print("equilateral")
# elif (a==b and a!=c) or (c!=b and c==a) or (b==c and b!=a):
#     print("isosceles")
# else:
#     print("scalene")
#
# qn6

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("Normal weight")
elif 25 <= bmi < 29.9:
    print(" Overweight")
else:
    print("Obese")