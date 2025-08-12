# While 

# Syntax: # initialize the var's used in bool_cond
#           while bool_cond:
                #  Logic
                # Updation of Looping var

# WAL to print upto n natural numbers.

# n = 4
# expected o/p: 1 2 3 4
#               3 4 
#               2 3 4

# i ==> looping var
# n ==> conditional var

n = int(input("Enter number:"))
i = 2
while i <= n:
    print(i, end = " ")
    i += 1
print("Program Executed")
print("Last i ",i)    

