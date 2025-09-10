detail={'name':'akhinash','age':24,'place':'ekm'}
# # print(detail)
# # print(detail['name'])
# # print(len(detail))
# # print(detail.keys())
# # print(detail.values())
print(detail.items())
fruits={'apple':1,'mango':1}
# #
fruits['orange']=3
print(fruits)
# # fruits.update({'job':'manager'})
# # print(fruits)
# # fruits.update({'game':'gta','movie':'sanadreas'})
# # print(fruits)
#
dic={'a':1,'b':2,'c':3,'d':4}
dic.popitem()
print(dic)
#
# dic_copy=dic.copy()
# print(dic_copy)
#
# #checking if a key is present in dictionary
#
# print('a' in dic)
# #checking if a value is present in dictionary
# print(3 in dic.values())
#
# #removing dictionary items
# del dic['a']
# print(dic)

#
# my_set=set([1,2,3])
# print(my_set)
#
# set={1,2,3}
# print(set)

a={1,2,3,4}
b={6,7,2,3}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(b.difference(a))
print(a.symmetric_difference(b))
b.add(8)
print(b)
b.remove(8)
print(b)
b.discard(10)
print(b)
b.pop()
print(b)
