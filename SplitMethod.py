str = "Pentagon Space"
print(len(str)) # 14
print(str) # Pentagon Space
str1 = str.split() 
print(len(str1)) # 2
print(str1) # ['Pentagon', 'Space']

# Split Method - It will split the string whwnever the space occurs

# String is immutable - value cannot be changed

str = "rama is studying"
print(str) # rama is studying

str1 = str.replace("is", "was")
print(str1) # rama was studying

a = 10 # 10 vaalue is stored in a it will check in the memory allocation if 10 is not there it will allocate the memory a is pointing to the memory location 
b = 10 # b is also pointing to the same memry location
c = 10

print(a) # -----|
print(b) #      | 10
print(c) # -----|

print(id(a)) # -----|
print(id(b)) #      | 12345
print(id(c)) # -----|

d = 20
e = 20
f = 20

print(d) # -----|
print(e) #      | 20
print(f) # -----|

print(id(d)) # -----|
print(id(e)) #      | 99000
print(id(f)) # -----|

print(a is b) #True
print(b is c) #True
print(c is f) #False
print(d is f) #True