# def countdown(n):

#     while n>0:
#         yield n
#         n-=1
        
# gen = countdown(3)

# print(next(gen))
# print(next(gen))
# print(next(gen))

    
# def my_generator():
#         yield 1
#         yield 2
#         yield 3
        
# for value in my_generator():
#      print(value)


# def count(n):
#     c=1
#     while c<=n:
#         yield c
#         c+=1        
# for i in count(5):
#     print(i)
    
    
# def my_generator():
#         yield 1
#         yield 2
#         yield 3
#         yield 4     
#         yield 5
        
# for value in my_generator():
#      c=value*value
#      print(c)

# def my_generator():
#     for i in range(6):
#         yield i*i
        
# for value in my_generator():
#      print(value)

def my_generator():
    for i in range(11):
        if i%2==0 and i!=0:
            yield i 
            
for value in my_generator():
     print(value,end=" ")
        