# Even or odd
# WAP to check whether the given i/p number is even or odd

# def EvenOdd(n):
#     if n % 2 == 0:
#         print(f"{n} is Even")
#     else:
#         print(f"{n} is Odd")

# n = int(input("Enter a number: "))
# res = EvenOdd(n)   

# flag --> It hiolds a Boolean value
# res -->
# I/p and O/p Stmts try to keep outside the function

# def isEvenOdd(n):
#     if n%2 == 0:
#         return True # Even
#     else:
#         return False # Odd
    
# n = int(input("Enter a number: "))
# flag = isEvenOdd(n)
# if flag:
#     print(f"{n} is Even")
# else:
#     print(f"{n} is Odd")    

# Code Optimization logic:

# def isEvenOdd(n):
#     return n%2 == 0

# n = int(input("Enter a number: "))
# flag = isEvenOdd(n)
# if flag:
#     print(f"{n} is Even")
# else:
#     print(f"{n} is Odd")  

# WAP to print all the even numbers in a user defined range

# def isEvenOdd(n):
#     return n%2 == 0

# start = int(input("Enter Start value: "))
# end = int(input("Enter End value: "))

# if start > end:
#     print("Invalid I/P")
# else: 
#     print("Even number: ")   
#     for i in range(start, end+1):
#         flag = isEvenOdd(i)
#         if flag:
#             print(i, end = " ")

# WAP to print all the evwn and odd numbers in a user defined range separately

# def isEvenOdd(n):
#     if n%2 == 0:
#         return True
#     else:
#         return False

# start = int(input("Enter Start value: "))
# end = int(input("Enter End value: "))

# if start > end:
#     print("Invalid I/P")
# else: 
#     print("Even number: ") 
 
#     for i in range(start, end+1):
#         flag = isEvenOdd(i)
#         if flag:
#             print(i, end = " ")

#     print("\nOdd number: ") 
#     for i in range(start, end+1):
#         flag = isEvenOdd(i)
#         if flag == False:
#             print(i, end = " ")
            

# WAP to print first "n" even numbers

# def isEvenOdd(n):
#     return n%2 == 0

# count = int(input("Enter num: "))
# series = 1
# print("Even numbers are: ")
# while count > 0:
#     flag = isEvenOdd(series)
#     if flag:
#         print(series, end = " ")
#         count -= 1
#     series += 1    

# def isEvenOdd(n):
#     return n%2 != 0

# count = int(input("Enter num: "))
# series = 1
# print("Even numbers are: ")
# while count > 0:
#     flag = isEvenOdd(series)
#     if flag:
#         print(series, end = " ")
#         count -= 1
#     series += 1  

def isEvenOdd(n):
    return n%2 != 0

count = int(input("Enter num: "))
series = 1
print("Even numbers are: ")
while count > 0:
    flag = isEvenOdd(series)
    if flag:
        print(series, end = " ")
        count -= 1
    series += 1
    else:
        print(series, end = " ")
        count -= 1
    series += 1