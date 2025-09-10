#mod1
#1 write a pgm to print time given in seconds to HH:MM:SS
# t=int(input("enter time in seconds"))
# tm=t//60
# ts=tm%60
# th=tm//60
# tm=tm%60
# print("time in HH:MM:SS---",th,":",tm,":",ts)

#2 area of a circle
# import math
# r=float(input('enter the radius of circle'))
# a=math.pi*r*r
# c=2*math.pi*r
# print("area=",a,"circumferenc=",c)

# #3
# a=int(input("enter the number"))
# if a%2==0:
#     print("even")
# else:
#     print("odd")

#4
# a=int(input("enetr the first num"))
# b=int(input("enter the second num"))
# if a>b:
#     print(a," is greater")
# elif b>a:
#     print(b," is grater")
# else:
#     print(" equal")

#5
# import math
# b=int(input("enter the number"))
# a=int(input("enter the number"))
# c=int(input("enter the number"))

class student:
    def __init__(self):
        self.name=input("name")
        self.rollno=int(input("roll no"))

    def dataprint(self):
        print("name:",self.name,"rollno:",self.rollno)

s=student()
s.dataprint()
