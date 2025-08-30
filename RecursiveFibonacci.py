# def recFibonacci(pos, n1, n2):
#     if pos <= 0:
#         return # We are not expecting any o/p
    
#     print(n1, end = " ")
#     recFibonacci((pos-1), n2, n1+n2)

# pos = int(input("Enter num: "))
# recFibonacci(pos, 0, 1)

# WAP to print the nth fibonacci number

def fibonacciNumber(n):

    if n == 0 or n == 1:
        return n
    
    return fibonacciNumber(n-1)+fibonacciNumber(n-2)

num = int(input("Enter num: "))
res = fibonacciNumber(num)
print(res)
