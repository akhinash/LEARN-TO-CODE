import re

# text="hello world"
# result= re.match(r'world',text)

# if result:
#     print("match")
# else:
#     print("not match")

# import re

# text="Welcome to python"
# result= re.search(r'to',text)

# if result:
#     print("search succesful")
# else:
#     print("not found")

# import re

# text="my num is 34457 and 764368"
# result= re.findall(r'\d+',text)

# print(result)

# import re

# text="my num is 34457 and 764368"
# result= re.sub(r'\d+','#',text)

# print(result)

# import re

# text="apple,bannana,grape"
# result= re.split(r',',text)

# print(result)

# import re
# text="my phone numbers are 7025950071 and 7894561230"
# result=re.findall(r'\d{10}',text)
# print(result)

# phone = "987-654-3210"
# pattern = r'^\d{3}-\d{3}-\d{4}$'

# if re.match(pattern,phone):
#     print("valid")
# else:
#     print("invalid")
    

# def validate_phone(phone):
#     pattern = r'^[6-9]\d{9}$'  
#     return bool(re.match(pattern, phone))


# print(validate_phone("9876543210")) 
# print(validate_phone("1234567890"))


def validate_mail(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


print(validate_mail("abc@gmail.com")) 


0
