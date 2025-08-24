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

# l = [1, 2, 3, 4]
# l2 = []
# for i in l:
#     l2+=[i]
# print(l)
# print(l2)    

# Second largest value in the list

# def SecondLargest(list1, N):
#     final_list = []

#     for i in range(0, N):
#         max1 = 0

#         for j in range(len(list1)):
#             if list1[j] > max1:
#                 max1 = list1[j]

#         list1.remove(max1)
#         final_list.append(max1)

#     print(final_list)               

# list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10]
# N = 2
# SecondLargest(list1, N)

# Remove the duplicate element in the list

# l = [1, 2, 3, 2, 3]
# res = []
# for i in l:
#     if i not in res:
#         res += [i]
# print(res) 

# Rotate a list to the left or right by k positions.

# Merge two lists into one sorted list

# l = [1,2,3,4,5]
# l1 = [11,22,33,44,55]
# l2 = []
# l2 = l + l1

# for i in range(len(l2)):
#     for j in range(i+1, len(l2)):
#         if l2[i] > l2[j]:
#             l2[i], l2[j] = l2[j], l2[i]
# print("Merged and sorted list:", l2)

# Find Common elements between two lists

# l = [1,2,3,4,5]
# l1 = [1,2,33,44,55]
# res = []
# for i in l:
#     for j in l1:
#         if i == j:
#             res += [j]
# print(res)

# Seperate a list into even and odd into two different lists

# l = [1,2,3,4,5,6,7,8]
# even = []
# odd = []
# for i in l:
#     if i%2 == 0:
#         even += [i]
#     else:
#         odd += [i]
# print(even)
# print(odd)  

# Find the difference between largest and smallest element in the list

# l = [1,2,3,7,8,4,5,6]
# largest = l[0]
# smallest = l[0]

# for i in l:
#     if i > largest:
#         largest = i
#     else:
#         smallest = i

# print(largest - smallest)        

# Count how many elements are greater than a given number n

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# n = int(input("Enter a number: "))
# count = 0

# for i in l:
#     if i > n:
#         count += 1
# print(count)    

# Flatten a nested list Example: [[1, 2], [3, 4]] to [1, 2, 3, 4]

# l = [[1, 2], [3, 4]]
# l1 = []
# for i in l:
#     for j in i:
#         l1 += [j]
# print(l1)        

# Check if the list is sorted in asending order

# l = [1,2,3,4,5]
# res = True
# for i in range(len(l)-1):
#     if l[i]>l[i+1]:
#         res = False
#         break
# print(res)    

# Remove all elements from one list that are present in another list

# l = [1,2,3,4,5]
# l1 = [1,2,3,6,7]
# l2 = []

# for i in l:
#     if i not in l1:
#         l2.append(i)
# print(l2)

# Find the index of all occurrences of a given element in a list

# l = [1,2,3,1,1,1]
# j = 1
# c = 0
# for i in range(len(l)-1):
#     for j in l[i]:
#         if i == j:
#             c += 1
# print(c)    
# 
# WRONG        

# Split a list into chunks of size n.
# Example: [1,2,3,4,5,6] into chunks of 2 --> [[1,2],[3,4],[5,6]]

# l = [1,2,3,4,5,6]
# n = 2
# chunks = []
# for i in range(0, len(l), n):
#     data = l[i:i+n]
#     chunks.append(data)
# print(chunks)    
    
# Replace all negative numbers in a list with 0.

# l = [-1, -2 ,-3, 3, 4, 5]
# for i in range(len(l)):
#     if l[i] < 0:
#         l[i] = 0
# print(l)      

# Interchange the first and last element of the list

# l = [1,2,3,4,5]
# l[0], l[len(l)-1] = l[len(l)-1], l[0]
# print(l)

# 



