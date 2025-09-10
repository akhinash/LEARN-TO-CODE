# n=int(input('enter the limit'))
# a=0
# b=1
# c=0
# while c<=n:
#     print(a)
#     temp=a+b
#     a=b
#     b=temp
#     c=c+1



n=int(input("enter the number"))
if n<2:
    print("not prime")
else:
    i=2
    while i<n and n %i==0:
        print("not prime")

        i=i+1
    else:
        print("prime")