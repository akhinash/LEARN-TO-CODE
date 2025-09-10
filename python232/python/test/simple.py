# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print("*",end="")
#         j=j+1
#     print()
#     i=i+1
#
from idlelib.window import add_windows_to_menu

# i=1
# limit=5
# while i<=limit:
#     k=1
#     while k<=(limit-i):
#         print(" ",end="")
#         k=k+1
#
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i+1

# size = int(input("enter size"))
# for row in range(size, 0, -1):
#     for sp in range(1, size - row):
#         print(" ", end="")
#     for col in range(1, row + 1):
#         print("* ", end="")
#
#     print()


# row=5
# for i in range(1,row+1):
#     print(" " * (row - i) + "*" * (2 * i - 1))
# for i in range(row-1,0,-1):
#     print(" " * (row - i) + "*" * (2 * i - 1))
#
print("insert card")
b=1000
a=int(input("pls enter your pin"))
if a==0000:
    c=input("select the service\n 1.balance enquiry\n 2.withdraw\n 3.deposit")
    if c=="1":
        print(b)
    elif c=="2":
        d=int(input("enter the amount to be withdraw"))
        if d>b:
            print("insufficient balance")
        else:
            b=b-d
            print("balance amount",b)

    elif c=="3":
        g=int(input("enter the amount to deposit"))
        b=b+g
        print("balance amount",b)

    else:
        print("invalid")



