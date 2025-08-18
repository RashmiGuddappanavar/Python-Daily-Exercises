# String reverse

# n = input("Enter a number: ")
# res = ""
# for i in n:
#     res = i + res 
# print(res) 

# Reverse a number

# logic:-
# Th H T U
# 5  8 2 3 ==> (0*10)+3=3
#              (3*10)+2=32
#              (32*10)+8=328
#              (328*10)+5=3285

# a) extract the digit
# b) align the extracted  digit by making space (*10)
# c) Remove the digit

# num = int(input("Enter a number: "))
# temp = num
# if num <0:
#     num = num * -1
# rev = 0
# while num > 0:
#     rem = num%10
#     rev = (rev*10)+rem
#     num = num//10
# if temp < 0:
#     rev = rev * -1    
# print(f"The reversal of {temp} is: {rev}")    

# def ReverseNumber(num):
#     temp = num
#     if num <0:
#         num = num * -1
#     rev = 0
#     while num > 0:
#         rem = num%10
#         rev = (rev*10)+rem
#         num = num//10
#     if temp < 0:
#         rev = rev * -1 
#     print(f"The reversal of {temp} is: {rev}")
       
# num = int(input("Enter a number: "))
# r1 = ReverseNumber(num)

# WAP to reverse each individual number among a range of val's 

# I/P:
#                sr = 12                      er = 16
#                The reversal of 12 is 21
#                The reversal of 13 is 31
#                The reversal of 14 is 41
#                The reversal of 15 is 51
#                The reversal of 16 is 61


start = 12
end = 16
for i in range(start, end):
    rem = n%10
    rev = (rev*10)+rem
    n = n//10
    print(f"The reversal of {n} is {rev}")    



