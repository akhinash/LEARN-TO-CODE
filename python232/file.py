# f= open("sample.txt","w")
# f.write("hello world\n")
# f.write("welcome to python")
# f.close()

# f=open("sample.txt","a")

# f.write("\nnew line")
# f.close()

# f=open("sample.txt","r")
# # print(f.read())
# print(f.readlines())
# # print(f.readline())

# f.close()

with open("sample.text","w") as f:
    content = f.write("hello b")
print(content)