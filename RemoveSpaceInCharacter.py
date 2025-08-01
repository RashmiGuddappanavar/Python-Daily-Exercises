# Write a program to remove the spaces between the characters

str = input("Enter a String: ")
i=0
newstr = ""

while (i <= len(str)-1):
    data = str[i]
    if (data == " "):
        i+=1
    else:
        newstr+=data 
        i+=1   
print(newstr)        