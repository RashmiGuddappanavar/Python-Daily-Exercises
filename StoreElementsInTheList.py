# l = []
# i = 0
# while i <= 4:
#     print("Enter the value: ")
#     data = int(input())
#     l.insert(i, data)
#     i+=1
# print(l)
# print()
# i = 0
# while i <= 4:
#     print(l[i])
#     i += 1

# Write a program to print only even numbers from the list

def Even(num):
    if (num % 2 == 0):
        return True
    else:
        return False
    
l = []
i = 0
while i <= 4:
    print("Enter the value: ")
    data = int(input())
    l.insert(i, data)
    i+=1
print(l) # [10, 11, 12, 13, 14]

# i = 0
# while i <= 4:
#     ext = l[i]
#     status = Even(ext)
#     if (status == True):
#         print(l[i])
#     i += 1    

k = list(filter(Even,l))
print(k) # [10, 12, 14]