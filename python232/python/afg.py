# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Get range from user
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

# Print prime numbers in the range
print(f"Prime numbers between {start} and {end}:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")
