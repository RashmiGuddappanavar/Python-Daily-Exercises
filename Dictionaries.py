# Maximun num
# marks={'eng':100,'math':99,'science':95}
# maxx=0
# for key,val in marks.items():
#     if maxx<val:
#         maxx=val
#         k=key
# print(f"{k}:{maxx}")

# Merge two dict
# marks2={'Kan':100,'physics':90}
# for key,val in marks.items():
#     marks2[key]=val
# print(marks)

# Swap 2 dict (marks2)
# swaped_dict={}
# for key,val in marks2.items():
#     swaped_dict[val]=key
# print("Swapped dict of marks2:",swaped_dict)

# Sort by keys(marks1)
# d={'b':2,'a':1,'c':3}
# sorted_items=sorted(d.keys())
# print(sorted_items)

# Two lists into dictionary using zip
# l1=['a','b','c']
# l2=[1,2,3]
# d={}
# for l1,l2 in zip(l1,l2):
#     d[l2]=l1
# print(d)

# Remove all duplicate values from a dictionary

# d = {'b':2,'a':1,'c':1}
# d1 = {}
# temp = []
# for key,val in d.items():
#     if val not in temp:
#         temp.append(val)
#         d1[key] = val
# print(str(d1))         

# Check if two dictionaries are equal

# a = {1:"a", 2:"b", 3:"c"}
# b = {1:"b", 2:"b", 3:"c"}

# if a == b:
#     print("True")
# else:
#     print("False")   

# Frequency Counter
# Given a string, count how many times each character appears and store it in a dictionary.

# a = "Rashmi"
# d = {}
# c = 0
# for i in a:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
#     c += 1

# print(d)
# print(c)            

# Word Occurrence
# Given a sentence, count how many times each word appears.

# a = "This is my book is"
# d = {}
# c = 0
# for i in a.split():
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
#     c+=1

# print(d)
# print(c)            

# Swap Keys and Values
# Given a dictionary, create a new dictionary by swapping keys and values.

# a = {1:"a", 2:"b", 3:"c", 4:"d"}
# d = {}
# for key,val in a.items():
#     d[val] = key

# print(a)
# print(d)    

# Merge Dictionaries
# Write a program to merge two dictionaries into one.

# a = {1:"a", 2:"b", 3:"c", 4:"d"}
# b = {5:"e", 6:"f"}
# c = {}
# for key,val in a.items():
#     c[key] = val
# for key,val in b.items():
#     c[key] = val    

# print(c)    

a = {1:"a", 2:"b", 3:"c"}
b = {1:"a", 4:"b", 5:"e"}
d = {}
for key, val in a.items():
    for key, val in b.items():
        if d[key]


