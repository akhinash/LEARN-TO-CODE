from selectors import SelectSelector

# i=2
# while i%2==0 and i<20:
#     print(i)
#     i=i+2
#
# a=input("input")
# b="enetr input"
# while a!='exit':
#     print(b)
#

b=5
while b>=1:
    print(b)
    b=b-1
print("blast opff")



while True:
    num = int(input("Enter a positive integer: "))  # Get user input and convert to an integer
    if num > 0:
            print(f"Valid input received: {num}")
            break  # Exit the loop if the number is positive
    else:
            print("Please enter a positive integer.")

