# l = [1, 2, 3, 4]
# print(l)

# # Access the first and last element of a list

# a = l[0]
# b = l[len(l)-1]
# print(a,b)

# # Find the length of a list without using len()

# count = 0
# for i in l:
#     count += 1
# print(count)    

# # Append a new element to a list

# l1 = l.append(7)
# print(l)

# # without append method

# n = int(input("Enter a number to add in the list: "))
# l = l + [n]
# print(l)

# # Insert an element at a given position in a list

# l2 = l.insert(0, 9)
# print(l)

# # Remove a given element from the list

# l3 = l.remove(1)
# print(l)

# # Without remove 

# l = [1, 2, 3, 4]
# num = int(input("Enter a num to remove: "))

# if num in l:                 # check if number is in the list
#     pos = l.index(num)       # find its position
#     l = l[:pos] + l[pos+1:]  # create new list without that element
# print(l)

# # Remove the element at a specific index

# del l[2]
# print(l)

# # OR

# l = [10, 20, 30, 40, 50]
# index = int(input("Enter index to remove: "))

# if 0 <= index < len(l):           # check valid index
#     l = l[:index] + l[index+1:]   # skip that index
#     print(l)
# else:
#     print("Invalid index")

# Reverse a list without using .reverse() or slicing

# l = [1, 2, 3, 4]
# res = []
# for i in l:
#     res = [i] + res
# print(res)    

# Find the maximum and minimum value in a list without using max() or min()

# l = [1, 2, 3, 4]
# min = l[0]
# max = l[0]
# for i in l:
#     if i < min:
#         min = i
#     if i > max:
#         max = i   

# print(f"{min} is minimum")
# print(f"{max} is maximum")

# Sum all elements of a list without using sum()

# l = [1, 2, 3, 4]
# add = 0
# for i in l:
#     add += i
# print(add) 

# Check if an element exists in a list (without using in)

# l = [1, 2, 3, 4]
# n = int(input("Enter a element: "))
# for i in range(len(l)):
#     if n == l[i]:
#         print(f"{n} Element exists at index {i}")

# Make a new list containing only even numbers from a given list

# l = [1, 2, 3, 4]
# l2 = [i for i in l if i%2 == 0]
# print(l2)

# Square each element of a list

# l = [1, 2, 3, 4]
# l2 = [i**2 for i in l ]
# print(l2)

# Copy a list without using .copy() or list()

l = [1, 2, 3, 4]
l2 = []
for i in l:
    l2+=[i]
print(l)
print(l2)    

# 
 
