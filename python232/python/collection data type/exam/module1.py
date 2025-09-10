#
# time=input("Enter time in seconds")
# time=int(time)
# timeinmin=time//60
# timeinsec=time%60
# timeinhr=timeinmin//60
# timeinmin=timeinmin%60
# print("HH:MM::SS--",timeinhr,"::",timeinmin,"::",timeinsec)

#2

# import math
# r=int(input("enter the radius"))
# area=2*math.pi*r
# cir=math.pi*r*r
# print("area=",area,"circum=",cir)
#
# #3

# i=int(input("enter a num"))
# if(i%2==0):
#     print("even")
# else:
#     print("odd")

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a > b:
#     greater = a
# else:
#     greater = b
# while True:
#     if greater % a == 0 and greater % b == 0:
#         lcm = greater
#         break
#     greater += 1
# print("LCM is", lcm)

a=int(input("enter num"))
c=str(a)
b=len(str(a))
if b!=3:
    print("error")
else:
    sum=0
    for i in c:
        sum=sum+int(i)**3
    if sum==a:
        print("armstrong")
    else:
        print("not armstrong")

