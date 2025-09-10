
#5
# a=input("enter a string")
# rev=a[::-1]
# if a==rev:
#     print("palindrome")
# else:
#     print("not palindrome")

#6
# a=int(input("enter the number"))
# if a%2==0:
#     print("even")
# else:
#     print("odd")

#7

# lisst=['a','e','i','o','u']
# alpha=input("enter the single alphabet")
# if alpha in lisst:
#     print("vowel")
# else:
#     print("not vowel")

#SECTION C

#2
# print("insert card")
# a=int(input("enter pin"))
# b=1000
# if a==0000:
#     c=input("select the service\n 1.Balance enquiry \n 2.withdraw\n 3.deposit\n")
#     if c=='1':
#         print(b)
#     elif c=='2':
#         d=int(input("enter the amount to be withdraw"))
#         if d>b:
#             print("insufficient fund")
#         else:
#             b=b-d
#             print("balance amount: ",b)
#     elif c=='3':
#         s=int(input("enter the amount to deposit"))
#         b=b+s
#         print("balance amount: ",b)
#     else:
#         print("service invalid")
#   
# else:
#     print("incorrect pin")


# #3
b={"english":80,"maths":90,"science":85}
total=sum(b.values())
subject=len(b.keys())
avg=total/subject
print("average marks: ",avg)