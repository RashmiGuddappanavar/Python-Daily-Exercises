def countdig(n, count):
    if n <= 10:
        return count
    n//=10
    count+=1
    return countdig(n, count)

n = int(input("Enter num : "))    
res = countdig(n, 0)
print(f"The count of digits {n} is {res}")