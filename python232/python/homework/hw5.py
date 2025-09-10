a=input('enter a string')
c=list(a)
b=list(a)
b.reverse()
if b==c:
    print('palindrome')
else:
    print("not palindrome")