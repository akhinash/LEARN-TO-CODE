# l=['anu',18,88]
# print(l)
# print(l[0])
# print(l[1])
# print(l[2])
# print(l[-3])
# print(l[-2])
# print(l[-1])

#pop()
# age=[21,29,23,45,32,26]
# print(age)
# new=age.pop()
# print(age)
# print(new)



a=[22,21,25,32,33]
new=a.pop(3)
print(a)
print(new)
#

#APPEND()
fruits=["apple","banana","cherry"]
fruits.append("orange")
print(fruits)

stud=["achu",22,85.5]
print(type(stud))
stud.pop()
stud.append(23.5)
print(stud)

lisst=[]
lisst.append(1)
lisst.append(2)
lisst.append(3)
print(lisst)

# veg=["carrot",'cabbage']
# fruits=['apple','mango']
# fruits.append(veg)
# print(fruits)
#
list=['Akhinash',24,'stu']
list[0]='my name is Akhinash'
print(list)

#
# fruits=['apple','banana']
# fruits.insert(0,'orange')
# print(fruits)
#
# mylist=[1,2,2,3,8,6,4]
# mylist.remove(2)
# mylist.sort()        #default sorting ascending ordr
# print(mylist)
#
# num=[8,6,7,3,4,1]
# num.sort(reverse=True) #descending order
# print(num)

num=[1,2,2,1,3,3]
print(num.index(1))
print(len(num))

# num=['one','two','one','three','two']
# print(num.index('two'))
# print(len(num))

l=[1,2,10,12]
print(l[1:3])
print(l[1:])
print(l[:])
print(l[:3])
del l[:3]
print(l)
#
# l.clear()
# print(l)

a=[1,23,45,12,34,22,345,"anupam"]
print(a[1:])
print(a[:3])