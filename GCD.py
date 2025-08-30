# n1 = int(input("Enter the first number: "))
# n2 = int(input("Enter the Second number: "))
# larger = n1
# if n2 > n1:
#     larger = n2

# for i in range(2, larger+1):
#     if n1%i == 0 and n2%i ==0:
#         gcd = i

# print(f"The GCD of {n1} and {n2} is: {gcd}")         

def isGCD(n1, n2):
    larger = n1
    gcd = 1
    
    if n2 > n1:
        larger = n2

    for i in range(2, larger+1):
        if n1%i == 0 and n2%i ==0:
            gcd = i   

    return gcd == 1

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the Second number: "))   
flag = isGCD(n1, n2)  
if flag:
    print("\nCo-Prime Number")
else:
    print("\nNot Co-Prime Number")   