# # Arm Strong Number
# # -----------------------------------------------------------------------------------------

# # - It is the sum of exponent val(base --> extracted digit and power --> count of digit ) is same as the original number then it is said to be ASN

# def countTheDigit(n):

#     # if n < 0: # Checking for negative num
#     #     n = -(n) # Or n = n * -1
#     c = 0    
#     while n > 0:
#         n = n // 10
#         c += 1
#     return c

# n = int(input("Enter a number: "))
# temp = n
# if n < 0:
#     n = -(n)
# pow = countTheDigit(n)
# asn = 0

# while n > 0 :
#     base = n % 10
#     asn = asn + (base**pow)
#     n = n // 10

# if temp < 0:
#     asn = -(asn)

# if temp == asn:
#     print(f"{temp} is a ASN")
# else:
#     print(f"{temp} is not a ASN")  

# ASN in range 

def asn(n):
    asn = 0
    num = n
    power = len(str(num))

    while num > 0:
        base = num % 10
        asn = asn + (base ** power)
        num//=10
    return asn
    
n = int(input("Enter a number: "))
temp = n        
if temp == asn(n):
    print(f"{temp} is a ASN")
else:
    print(f"{temp} is not a ASN") 






