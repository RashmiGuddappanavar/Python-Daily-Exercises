def happyNumber(n):
    if n == 1:
        return True
    elif n == 4:
        return False
    
    sum = 0
    while n > 0:
        base = n % 10
        sum = sum + (base**2)
        n = n//10
    return happyNumber(sum)    

num = int(input("Enter a number: "))
res = happyNumber(num)
if res:
    print(f"{num} is a happy number")
else:
    print(f"{num} is not a happy number")    

# Note : How to repeat a repeated logic
# - Nested loop
# - Loop inside recursive function