#1
i=1
while i<=5:
    j=1
    while j<=i:
        print("*",end=' ')
        j=j+1
    print()
    i=i+1

# #2
i=1
limit=5
while i<=limit:
    k=1
    while k<=(limit-i):
        print("",end=" ")
        k=k+1
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    print()
    i=i+1
i=limit-1
while i>0:
    k = 1
    while k <= (limit - i):
        print("", end=" ")
        k = k + 1
    j = 1
    while j <= i:
        print("*", end=" ")
        j = j + 1
    print()
    i=i-1

#3
def anagram(str1,str2):
    return sorted(str1)==sorted(str2)
print(anagram('tree','reet'))

#4
def tri(a,b,c):
    s=[a,b,c]
    if s[0]**2+s[1]**2==s[2]**2:
        print("right")
    else:
        print("not right")
tri(2,3,4)

#5
#
for i in range(1,101):
    if i%2==0:
        print(i)

#6
n=int(input('enter the limit'))
a=0
b=1
c=0
while c<=n:
    print(a)
    temp=a+b
    a=b
    b=temp
    c=c+1

#7

l=list(map(int, input("Enter the Sequence with spaces: ").split()))
d=l[1]-l[0]
for i in range(l[0],(l[-1]+1),d):
    if i in l:
        continue
    else:
        print(f"{i}  is missing, Adding to the list")
        l.append(i)
l.sort()
print(f"list after sort:\n",l)




