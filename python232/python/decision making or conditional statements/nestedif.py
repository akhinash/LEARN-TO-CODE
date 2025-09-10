# x=5
# if x>3:
#     if x<7:
#         print("x is bw 3 and 7")
#     else:
#         print("x is greater than 7")
#
# else:
#     print("x is less than or equal to 3")




# num = int(input("enter the num"))
# # if num >= 0:
#     if num == 0:
#         print("zero")
#     else:
#         print("positive")
# else:
#     print('negative')



# num=int(input("enter the number"))
# if num%2==0:
#     if num>10:
#         print("num is even and greater than 10")
#     else:
#         print('num is even ')
# else:
#     print("num is odd")




mark=int(input("enter your marks"))
att=int(input("enter attendance percentage"))

if mark>80:
    if att>70:
        print("elgible for scholarship")
    else:
        print("not elgible due to shortage of attendance")
else:
    print("not elgible for the scholarship")