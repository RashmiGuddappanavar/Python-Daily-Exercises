# print("Enter a String: ")
# str = input()
# i = 0
# result = ""
# while(i <= len(str)-1):
#     data = str[i]
#     ascii = ord(data)
#     if (ascii >=97 and ascii <=  122):
#         newascii = ascii - 32
#         convchar = chr(newascii)
#         result += convchar
#     else:
#         result += data
#     i+=1   
# print(result)    

# Swapcase

# print("Enter a String: ")
# str = input()
# i=0
# result=""
# while (i <= len(str)-1):
#     data = str[i]
#     ascii = ord(data)
#     if (ascii >= 65 and ascii <= 90):
#         newascii = ascii + 32
#         convchar = chr(newascii)
#         result += convchar
#     else:
#         newascii = ascii - 32
#         convchar = chr(newascii)
#         result += convchar
#     i+=1
# print(result)            

print("Eneter a String: ")
str = input()

str1 = str.upper()
print(str1)

str2 = str.lower()
print(str2)

str3 = str.swapcase()
print(str3)
