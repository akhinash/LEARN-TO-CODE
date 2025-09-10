#syntax
#for i in iterable item:
#           body of the loop
#
#
#
#
# list=[1,2,3,4,5]
# i=0
# while i<len(list):
#     print(list[i])
#     i=i+1
#
# list=[1,2,3,4,5]
# for i in list:
#     print(i)


# a=[22,45,65,23,77]
# max=0
# for i in a:
#     i>max
#     max=i
# print(max)

# for i in range(100,0,-1):
#     print(i)
# for i in range(2,51,2):
#     print(i)


# num=int(input("enter number"))
# if num<2:
#     print(num,"not prime")
# else:
#     for i in range(2,num//2+1):
#         if num%i==0:
#             print(num,"is not a prime")
#             break
#     else:
#         print(num,"is prime")
#
# numbers=[]
# for i in range(5):
#     num=int(input("enter num"))
#     if num>=5 and num<=25:
#         numbers.append(num)
#     else:
#         print("invalid")
# print(numbers)

# numbers=[]
# count=0
# while True:
#     num=int(input("enter number"))
#     if num >= 5 and num <= 25:
#         numbers.append(num)
#         count+=1
#     else:
#         print("invalid")
#     if count>=5:
#         break
# print(numbers)
#
# a=(1,2,3,4,'k')
# for i in a:
#     print(i)


# a={"k1":'abc','k2':'cbd','k3':'gbd'}
# for key in a:
#     print('key',key)
# for value in a.values():
#     print(value)
# for b in a.items():
#     print(b)

key=["name",'age','city']
values=['akhinash',24,'ekm']
dic=dict(zip(key,values))
print(dic)
