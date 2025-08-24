# def printnum(n):
#     if n <= 0:
#         return 
#     printnum(n - 1)
#     print(n, end = " ")
    
# n = int(input("Enter num"))
# printnum(n) 

# def printnum(n):
#     if n <= 0:
#         return 
#     print(n, end = " ")
#     printnum(n - 1)
# n = int(input("Enter num"))
# printnum(n) 

# def printnum(n, i = 1):
#     if i > n:
#         return     
#     print(i)
#     printnum(n, i+1)
#     print(i)
    
# n = int(input("Enter num"))
# printnum(n) 

# OR

def dispnum(i, n):
    if i > n:
        return 
    print(i)
    dispnum(i+1, n)
    print(i)

n = int(input("Enter num: "))
dispnum(1, n)

# O/P: Enter num: 4
# 1
# 2
# 3
# 4
# 4
# 3
# 2
# 1

# def printnum(n):
#     if n == 0:
#         return     
#     print(n)
#     printnum(n-1)
#     print(n)
    
# n = int(input("Enter num"))
# printnum(n)
