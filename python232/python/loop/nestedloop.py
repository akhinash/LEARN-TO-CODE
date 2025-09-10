#nested while loop
# i=1
# while i<=2:
#     j=1
#     while j<=3:
#         print(i,j)
#         j=j+1
#     i=i+1
#

# i=1
# while i<=5:
#     j=1
#     while j<=5:
#         print("a",end=' ')
#         j=j+1
#     print()
#     i=i+1


i=1
while i<=5:
    j=1
    while j<=i:
        print("*",end=' ')
        j=j+1
    print()
    i=i+1
#
# i=5
# while i>=1:
#     j=1
#     while j<=i:
#         print("a",end=' ')
#         j=j+1
#     print()
#     i=i-1

i=1
limit=5
while i<=5:
    k=0
    while k<=(limit-i):
        print('',end=' ')
        k=k+1
    j=1
    while j<=i:
        print("*",end=' ')
        j=j+1

    print()
    i=i+1

