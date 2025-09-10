# str=('java is a programing language')
# b=str[4:]
# print('python'+b)
#
# str=('java is a programing language')
# print(str.replace('java','python'))

# s="programming"
# print(s[3:7])

#concatenation
'''print('hello'+'world')
l1=[1,2,3,4]
l2=[4,8,7,4]
print(l1+l2)
from idlelib.replace import replace

#repeatition
print(2*2)
print("2"*2)
print("hello"*3)

l=[1,'a','carrot',5.8,'v']
print(l[1])
print(l[2][2])
l[2]='beetroot'
print(l)

seq=[3,4,10,5,7,1,2]
seq.sort()
print(seq[-2])

#swapping
a=90
b=50

tem=a
a=b
b=tem

print(a)
print(b)

'''

# a=90
# b=50
# a,b=b,a
# print(a,b)


# x=5
# y=10
# x,y=y,x
# print(x,y)

# l=[1,2,3,4]
#
# # c=l[0]
# # l[0]=l[1]
# # l[1]=c
# # print(l)
# l[1],l[3]=l[3],l[1]
# print(l)

# l=[1,55,1,4,10,9]
# l.sort()
# print("largest number=",l[-1])
# print("smallest",l[0])

# a="abc"
# c=list(a)
# c.reverse()
# print(c)
#
# text = input("Enter a string: ")
# char_list = list(text)
# c=char_list.reverse()
# print(c)
#
# a = input('Enter a string: ')  # Take user input
# c = list(a)  # Convert string to list of characters
# b = list(a)  # Create a copy of the list
# b.reverse()  # Reverse the list in place
#
# # Compare reversed list with the original
# if b == c:
#     print('Palindrome')
# else:
#     print('Not palindrome')

#
# l=list(map(int, input("Enter the Sequence with spaces: ").split()))
# d=l[1]-l[0]
# for i in range(l[0],(l[-1]+1),d): # range(start,stop,step_value)
#     if i in l:
#         continue # continue to the next
#     else:
#         print(f"{i}  is missing, Adding to the list") # if  element is missing then add it to the list
#         l.append(i)
# l.sort()
# print(f"list after sort:\n",l)
#



a=[1,2,3]
b=[3,2,1]
c=set(a).intersection(b)
print(c)
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
#
# # Find common elements
# common_elements = set(list1).intersection(list2)
# print("Common elements:", common_elements)