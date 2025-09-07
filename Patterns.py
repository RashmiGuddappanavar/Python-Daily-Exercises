# Patterns:
# - It is the combination of rows and cols
# - ==> Sleeping / Horizontal lines / rows
# - ==> Standing / vertical lines / cols

# "n" ==> total num of rows to be printed in the pattern
#                        4 <= n <= 15
# 
# 2 Types:
#        1. Non - Combinational: Right angle Tri, Square,...
#           - direct "n" val will be taken as I/P
# 
#        2. Combinational: K pattern, Diamond, Butterfly
#           - "(2 * n)" val will be taken as I/P
# 
# Varities: Star, Hollow, Number, Alphabetic

# print("Hello")
# print("World")
# print()
# print("Hii")
# print("Hello", end = " ")
# print("World")

# end - Predefined attribute
# It Moves the control to the beginning of the next line
# If any argumnet i passed then display on the O/P screen and move the control to the beggining of the next line
#  Once u move the controll to the next line u can never get it backto the previous line

# print("*")

# print("--------------------------")

# n = int(input("Enter num:"))
# for  i in range(1, (n+1)):
#     print("*")
# 
# Input: 3
# Output:
# *
# *
# *

# print("--------------------------")

# n = int(input("Enter num:"))
# for  i in range(1, (n+1)):
#     print("*", end = " ")
#
# Input: 4
# Output:
# * * * * 

# print("--------------------------")    

# n = int(input("Enter num: "))
# for j in range(1,(n+1)):
#     print("\n==========")
#
# Input: 3
# Output:
# ==========
# ==========
# ==========

# Square   n = 4
# *****
# *****
# *****
# *****   
# ------------------------------------------------------------------------------------------------------------------------------------------------
# Square pattern
# n = int(input("Enter num: "))

# for i in range(1, n+1):   # Rows
#     for j in range(1, n+1):   # Columns
#         print("*", end=" ")
#     print()   # Move to the next line after each row
#
# Input: 4
# Output:
# * * * * 
# * * * * 
# * * * * 
# * * * * 

# ------------------------------------------------------------------------------------------------------------------------------------------------
# Note:

# Outer loop is for rows & inner loop is for cols, bcz once the controlis moved
# to the next line we cannot bring it back to the previous line using simple loops. 

# "i" loop is always dependent on "n" val   
# "j" loop is dependent on "n" or "i" or "any 3rd var"
# ------------------------------------------------------------------------------------------------------------------------------------------------


# Triangular 
# ------------------------------------------------------------------------------------------------------------------------------------------------
# a)LHS Right Angled triangle

# n = int(input("Enter num: "))

# for i in range(1, n+1):    
#     for j in range(1, i+1):    
#         print("*", end="")     
#     print()                    
#
# Input: 4
# Output:
# *
# **
# ***
# ****

# 2) LHS Inverted right angle triangle
# ------------------------------------------------------------------------------------------------------------------------------------------------
# n = int(input("Enter num: "))

# for i in range(n, 0, -1):
#     for j in range(1, i+1):
#         print("*", end = "")
#     print()    
#
# Input: 4
# Output:
# ****
# ***
# **
# *

# RHS Right angle triangle
# ------------------------------------------------------------------------------------------------------------------------------------------------
# n = int(input("Enter number: "))
# for i in range(1, (n+1)):
#     for k in range(n , i, -1):
#         print(" ", end = "")
#     for j in range(1, (i+1)):
#         print("*", end = "")
#     print()
#
# Input: 4
# Output:
#    *
#   **
#  ***
# ****

# RHS Inverted Right angle triangle
# ------------------------------------------------------------------------------------------------------------------------------------------------
# n = int(input("Enter number: "))
# for i in range(1, n+1):
#     for k in range(1, i):
#         print(" ", end = "")
#     for j in range(n, (i-1), -1):
#         print("*", end = " ")
#     print()    
#
# Input: 4
# Output:
# * * * * 
#  * * * 
#   * * 
#    * 

# Pyramid
# ------------------------------------------------------------------------------------------------------------------------------------------------
# n = int(input("Enter number: "))
# odd = 1
# for i in range(1, n+1):
#     for k in range(n, i, -1):
#         print(" ", end="")

#     for j in range(1, odd+1):
#         print("*", end="")

#     print()
#     odd = odd + 2

# Input: 4
# Output:
#    *
#   ***
#  *****
# *******

# ------------------------------------------------------------------------------------------------------------------------------------------------
# n = int(input("Enter num: "))
# odd = (n*2)-1
# for i in range(1, (n+1)):
#     for k in range(1, i):
#         print(" ", end = "")

#     for j in range(odd, 0, -1):
#         print("*", end = "") 

#     print()   
#     odd -=2

# Enter num: 4
# *******
#  *****
#   ***
#    *

# ------------------------------------------------------------------------------------------------------------------------------------------------
# Combinational patterns

# n = int(input("Enter num: "))
# noc = 1
# for i in range(1, n*2):

#     for j in range(1, noc+1):
#         print("*", end = "")
#     print()    
#     if i < n:
#         noc+=1
#     else:
#         noc-=1

# Enter num: 4
# *
# **
# ***
# ****
# ***
# **
# *

# ------------------------------------------------------------------------------------------------------------------------------------------------

# n = int(input("Enter num: "))
# noc = 1
# for i in range(1, n*2):
#     for k in range(n, noc, -1):
#         print(" ", end = "")
#     for j in range(1, noc+1):
#         print("*", end = "")
#     print()    
#     if i < n:
#         noc+=1
#     else:
#         noc-=1    

# Enter num: 4
#    *
#   **
#  ***
# ****
#  ***
#   **
#    *

# ------------------------------------------------------------------------------------------------------------------------------------------------

# n = int(input("Enter num: "))
# noc = 1
# for i in range(1, n*2):
#     for k in range(n, noc, -1):
#         print(" ", end = "")
#     for j in range(1, noc+1):
#         print("* ", end = "")
#     print()
#     if i < n:
#         noc+=1
#     else:
#         noc-=1    

# Enter num: 4
#    * 
#   * * 
#  * * * 
# * * * * 
#  * * * 
#   * * 
#    *      

# ------------------------------------------------------------------------------------------------------------------------------------------------

# n = int(input("Enter num: "))
# noc = 1
# for i in range(1, (n*2)):
#     for k in range(((n*2)-1), noc , -1):
#         print(" ", end = "")
#     for j in range(1, (noc+1)):
#         print("* ", end = "")
#     print()
#     if i < n:
#         noc+=2
#     else:
#         noc-=2            

# Enter num: 4
#       * 
#     * * *
#   * * * * *
# * * * * * * *
#   * * * * *
#     * * *
#       *

# ------------------------------------------------------------------------------------------------------------------------------------------------
# n = int(input("Enter num: "))
# noc = n
# for i in range(1, (n*2)):

#     for j in range(1, (noc+1)):
#         print("* ", end = "")
#     print()

#     if i < n:
#         noc-=1
#     else:
#         noc+=1   

# ****
# ***
# **
# *
# **
# ***
# ****

# ------------------------------------------------------------------------------------------------------------------------------------------------

# n = int(input("Enter num: "))
# noc = n
# for i in range(1, (n*2)):
#     for k in range(1, (n-noc)+1):
#         print(" ", end = "")
#     for j in range(1, noc+1):
#         print("*", end = "")
#     print()

#     if i < n:
#         noc-=1
#     else:
#         noc+=1    

# ****
#  ***
#   **
#    *
#   **
#  ***
# ****

# ------------------------------------------------------------------------------------------------------------------------------------------------


# n = int(input("Enter num: "))
# noc = n
# for i in range(1, (n*2)):
#     for k in range(1, (n-noc)+1):
#         print(" ", end = "")
#     for j in range(1, noc+1):
#         print("* ", end = "")
#     print()

#     if i < n:
#         noc-=1
#     else:
#         noc+=1 

# * * * *
#  * * *
#   * *
#    *
#   * *
#  * * *
# * * * *

# n = int(input("Enter num: "))
# noc = 1
# nor = (n*2)-1
# for i in range(1, (n*2)):
#     for j in range(1, (n*2)):
#         if j <= noc or j >= nor:
#             print("*", end = "")
#         else:
#             print(" ", end = "")   
#     print()
#     if i < n:
#         noc+=1
#         nor-=1
#     else:
#         noc-=1
#         nor+=1
        
# *     *
# **   **
# *** ***
# *******
# *** ***
# **   **
# *     *

# Hallow Patterns

# n = int(input("Enter num: "))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == 1 or i == 5 or j == 1 or j == n:
#             print("*", end = "")
#         else:
#             print(" ", end = "")
#     print()             

# Enter num: 5
# *****
# *   *
# *   *
# *   *
# *****

# n = int(input("Enter num: "))
# if n%2 == 0:
#     n= n+1
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == 1 or i == 5 or j == 1 or j == n or i == j or (i+j) == (n+1):
#             print("*", end = "")
#         else:
#             print(" ", end = "")

#         print() 

# Enter num: 5
# *****
# ** **
# * * *
# ** **
# *****               

# n = int(input("Enter num: "))

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == 1 or i == 5 or i == j or (i+j) == (n+1):
#             print("*", end = "")
#         else:
#             print(" ", end = "")

#     print() 

# Enter num: 5
# *****
#  * *
#   *
#  * *
# *****

# n = int(input("Enter num: "))
# if n%2 == 0:
#     n= n+1
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if  j == 1 or j == n or i == j or (i+j) == (n+1):
#             print("*", end = "")
#         else:
#             print(" ", end = "")

#     print() 

# Enter num: 5
# *   *
# ** **
# * * *
# ** **
# *   *

# n = int(input("Enter num: "))
# for i in range(1, (n+1)):
#     for j in range(1, (i+1)):
        # if i == n or j == 1 or i == j:
        #     print("*", end = "")
        # else:
        #     print(" ", end = "")

#     print()            

# Enter num: 5
# *
# **
# * *
# *  *
# *****

# n = int(input("Enter num: "))
# for i in range(1, (n+1)):
#     for k in range(n, i, -1):
#         print(" ", end = "")

#     for j in range(1, (i+1)):
#         if i == n or j == 1 or i == j:
#             print("*", end = "")
#         else:
#             print(" ", end = "")

#     print()    

# Enter num: 5
#     *
#    **
#   * *
#  *  *
# *****

# n = int(input("Enter num: "))
# for i in range(1, (n+1)):
#     for k in range(n, i, -1):
#         print(" ", end = "")

#     for j in range(1, (i+1)):
#         if i == n or j == 1 or i == j:
#             print("* ", end = "")
#         else:
#             print("  ", end = "")

#     print()

# Enter num: 5
#     * 
#    * *
#   *   *
#  *     *
# * * * * *     

# n = int(input("Enter num: "))
# for i in range(n, 0, -1):
#     for j in range(1, (i+1)):
#         if i == n or j == 1 or i == j:
#             print("*", end = "")
#         else:
#             print(" ", end = "")    
#     print()   

# Enter num: 5
# *****
# *  *
# * *
# **
# *     

# n = int(input("Enter num: "))
# noc = 1
# for i in range(1, (n*2)):
#     for j in range(1, (noc+1)):
#         if j == 1 or j == noc:
#             print("*", end = "")
#         else:
#             print(" ", end = "")            
    
#     print()

#     if i < n:
#         noc+=1
#     else:
#         noc-=1    

# Enter num: 4
# *
# **
# * *
# *  *
# * *
# **
# *        

# n = int(input("Enter num: "))
# noc = 1
# for i in range(1, (n*2)):
#     for k in range(n, noc, -1):
#         print(" ", end = "")
#     for j in range(1, (noc+1)):
#         if j == 1 or j == noc:
#             print("*", end = "")
#         else:
#             print(" ", end = "")            
    
#     print()

#     if i < n:
#         noc+=1
#     else:
#         noc-=1 

# Enter num: 4
#    *
#   **
#  * *
# *  *
#  * *
#   **
#    *        

n = int(input("Enter num: "))
odd = (n*2)-1

for i in range(1, n+1):
    for k in range(1, i):
        print(" ", end="")

    for j in range(1, odd+1):
        if i == 1 or j == 1 or j == odd:
            print("*", end="")
        else:
            print(" ", end="")
    print()
    odd -= 2



