# Prime Number

# - The numbers which have exactly 2 factors (i.e,  1 and the number itself)
# - 1, 0 and negative number's can never be prime
 
# def PrimeNumber(n):
#     i = 1
#     count = 0

#     while i*i <= n:
        
#         if n % i == 0:
#             print(i, end = " ")
#             count += 1

#             if i != (n//i):
#                 print((n//i), end = " ")
#                 count += 1 

#         i += 1 

#     return count == 2

# n = int(input("Enter a number: "))
# flag = PrimeNumber(n)
# if flag:
#     print("\nPrime Number")
# else:
#     print("\nNot Prime Number")    

# WAP to print all the prime numbers present in the user defined range

def PrimeNumber(n):
    i = 1
    count = 0

    if n < 2:
        return False

    while i*i <= n:
        
        if n % i == 0:
            print(i, end = " ")
            count += 1

            if i != (n//i):
                print((n//i), end = " ")
                count += 1 

        i += 1 

    return count == 2
    
start = int(input("Enter a start value: "))
end = int(input("Enter the end value: "))

print("The Prime numbers between {start} and {end} are: ")
for num in range(start, end + 1):
    if PrimeNumber(num):
        print(num, end = " ")


# WAP to print all the prime numbers and Non-prime Numbers separetely present in a user defined range



# WAP to print "n" prime numbers
# WAP to print "n" Non-prime numbers  

