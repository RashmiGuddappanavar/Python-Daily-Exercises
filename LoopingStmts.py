# Looping Statement
#==================================================================================
# 1) for loop
        # a) with range()
        #      i) increment
        #     ii) decrement
        # b) without range()
# a) with range()

# syntax:- 
#           for var_name in range(start, stop, step):
                       # Logic
            # remaing stmts

#==================================================================================

# range - it's a predefined (in-built) function
#       - it helps to setup a mentioned range of values 
#       - Only "integer" arguments(start, till/stop/end, step)

#==================================================================================

# Note: 
# PVM is not capable of returning multiple sequence of values together at the same time (until a& unlessnit is not stored in a data structure)... for is used with range()

#==================================================================================

# start - from where PVM should begin to execute the range of values
#  - default start ==> 0

#==================================================================================

# stop/end:
# - Till where the range of values should get executed
# - Compulsory to pass
#==================================================================================

# step:- 
# - The difference between the current & the next value of the range
# - default step ==> +1

#==================================================================================

print(range(1, 5, +1)) 

print(range(3))

# print(range()) # Error

# Incrementing for loop
# Sytax: for var_name in range(start, actual end + 1, Positive step):
                        # logic
         # remaining stmts               

# WAL to print 1 - 4 in incrementing order 
# Expected O/P: 1 2 3 4
# start :- 1
# actual end:- 4 ==> loop:- (4 + 1) 

for i in range(1, 4+1, +1):
    print(i, end = " ")
print()    
print("Program executed")
print("Last i ", i ) 

# Tracing - Step by step analysis of the code on how it works during execution time.

# Step - +1 ===> positive step - incrementing loop
# start < mentioned end
# 1 < 5 ===> True
#            end val 'i' - 5

# decrementing for loop

# Syntax: for var_name in range(start, actual end - 1, negative step):
                #  Login
            #rem stmts

# rules:

# step shuld be compulsory -ve StopIteration
# start shld be grter thn EncodingWarning
# actual end minus 1

n=int(input())
for i in range(n, 2-1, -2):
    print(i, end =" ")
print()    
print("Program Executed")    
print("Last i ", i)

# 2. For without range():
    #    - it can be directly used in iterable objects or on group of elements
    #    - it moves only in forward direction
    #    - Here, the looping variable will directly holds each individual element

    #    Syntax:
    #    for var_name in 
    # 
    # Empty string is also a iterable object 
    # for i in 100:
    #     print(i, end = " ") #Error
    # 
    # for i in [100]:
    #     print(i, end = " ")
for i in 10, 20, 30:
    print(i, end = " ")
print("\n==============================================================================================================")

for i in 20, 10, -30:
    print(i, end = " ")
print("\n==============================================================================================================") 

for k in -100, 10, 20, 0 ,100 , -100, 10:
    print(k, end = " ")
print("\n==============================================================================================================") 

for i in "abc":
    print(i, end = " ")
print("\n==============================================================================================================")

for i in [1, 2, 3]:
    print(i, end = " ")
print("\n==============================================================================================================")

# For with range                                                          For without range

# Moves in forward direction                                              Supports incre & decre loop
# Looping variable directly hold each individual element one by one       It points to the index
# Inbuilt() func to get the index from iterable object                    No inbuilt required
# I/Ps shld be either iterable objects or grp of elements                 Only integers

l1 = [1, 2, 3]
for i in l1:
    print("ele: ", i, "index: ", l1.index(i))
print("\n==============================================================================================================")

for i in range (0, len(l1)):
    print("ele: ", l1[1], " index: ",i)
print("\n==============================================================================================================")

