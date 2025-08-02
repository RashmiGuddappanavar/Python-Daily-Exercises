# Membership Operator (in, not in)
# - It always return Boolean value
# - It is used to check whether  a single element is available in a group of element's or an iterable object or not

# Iterable Object - The obj's where we can store multiple individual elements into the same shared memory location Ex: List, set, dict, tuple 

s1 = "Aabbc12"
print("A" in s1)
print("abb" in s1)
print("123" not in s1)
print(1 in [11, 22, 33])
print("2" in "22")
print(3 in 33) #It cannot be used on single value data