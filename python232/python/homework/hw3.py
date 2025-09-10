#append

#qn1
# a=[1,3,4]
# a.append(10)
# print(a)
#
# #qn2
# name=input("enter your name")
# nlist=['achu','vchu']
# nlist.append(name)
# print(nlist)

#pop

# #qn1
# a=[1,3,4]
# a.pop()
# print(a)
#
#
# #qn2
# b=[1,3,4,6,7]
# b.pop(2)
# print(b)


#index

#qn1
# a=[1,3,4,5,6]
# print(a.index(5))

#qn2
# a=[]
# name1=input('enter name1')
# name2=input('enter name2')
# name3=input('enter name3')
# a.append(name1)
# a.append(name2)
# a.append(name3)
# index_name=input("enter name to find its index")
# if index_name==name1:
#     print(a.index(name1))
# elif index_name==name2:
#     print(a.index(name2))
# elif index_name==name3:
#     print(a.index(name3))
# else:
#     print('invalid')
#
# #insert

# #qn1
# a=[1,3,4,5,6]
# a.insert(2,10)
# print(a)

# qn2
# a=['achu','anu','akku']
# name=input('enter name')
# a.insert(0,name)
# print(a)


#REMOVE

#QN1
# a=[1,5,4,5,6,7]
# a.remove(5)
# print(a)

#qn2

a=['achu','nichu','michu']
name=input('enter the name to remove')
if name in a:
    a.remove(name)
    print(a)
else:
    print('name not in list')


#del

#q1
# a=[1,5,4,6,7]
# del a[2:3]
# print(a)
#
# #q2
# a=[1,5,4,6,7]
# del a[1:4]
# print(a)


#slicing
# #qn1
# a=[1,5,4,6,7]
# print(a[1:4])

#qn2
a=input("enter the numbers" )
print(a[-3:])




