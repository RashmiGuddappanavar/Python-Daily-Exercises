# def revaNum(n, rev):
#     if n <= 0:
#         return rev
    
#     rem = n%10
#     rev = (rev*10)+rem
#     n = n//10

#     return revaNum(n, rev)

# num = int(input("Enter num: "))
# res = revaNum(num, 0)
# print(res)

def revaNum(n, rev, temp):
    if n <= 0:
        return rev == temp
    
    rem = n%10
    rev = (rev*10)+rem
    n = n//10

    return revaNum(n, rev, temp)

num = int(input("Enter num: "))
flag = revaNum(num, 0, num)

if flag:
    print("Palindrome")
else:
    print("Not Palindrome")    