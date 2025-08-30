def isASN(n, pow, asn, temp):
    if n <= 0:
        return temp == asn
    base = n%10
    asn = asn + (base ** pow)
    n //= 10
    return isASN(n, pow, asn, temp)


def countdig(n, count):
    if n <= 0:
        return count
    n//=10
    count+=1
    return countdig(n, count)    

n = int(input("Enter num: "))
pow = countdig(n,0)
flag = isASN(n, pow, 0, n)
if flag:
    print("ArmStrong number")
else:
    print("Not ArmStrong Number")    