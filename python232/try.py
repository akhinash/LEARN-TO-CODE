# def AbyB(a , b):
# 	try:
# 		c = ((a+b) / (a-b))
# 	except ZeroDivisionError:
# 		print ("a/b result in 0")
# 	else:
# 		print (c)
# AbyB(2.0, 3.0)
# AbyB(3.0, 3.0)


# try:
# 	k = 5//0
# 	print(k)

# except ZeroDivisionError:
# 	print("Can't divide by zero")

# finally:
# 	print('This is always executed')


# try:
#     f=open("testfile.txt", 'r')
#     content=f.read()
#     print(content)
# except FileNotFoundError:
#     print("Error: File does not  exist.")  

# finally:
#     print("file operation completed")

# num=int(input("Enter a number: "))
# if num < 0:
#     raise ValueError("Negative numbers are not allowed")        
# else:
#     print("You entered:", num)


    
# x="text"
# if not isinstance(x, int):
#     raise TypeError("Only integers are allowed")        
    
    
    
# def check_age(age):
#     if age < 18:
#         raise ValueError("Age must be at least 18.")    
#     else:
#         print("Age is accepted.")
        
# check_age(20)
# check_age(15)   
# check_age(18)

num=int(input("Enter a number between 1 and 10: "))
if num < 1 :
    raise ValueError("Number is too small")
elif num > 10:
    raise ValueError("Number is too large")  
else:
    print("You entered:", num)