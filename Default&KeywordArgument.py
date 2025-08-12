'''
class Demo:
    def add(self,x=11,y=22,z=33):#--->default arguments
        print(x)
        print(y)
        print(z)
d1=Demo()
a=10
b=20
c=30
d1.add(a,b,c)#op-10,20,30
print("----------------------------------------------------")
d1.add(a,b)#op-10,20,33
print("----------------------------------------------------")
d1.add()#op-11,22,33
print("----------------------------------------------------")
d1.add(c)#op-30,22,33
print("----------------------------------------------------")
d1.add(z=c)#----->keyword arguments #op-11,22,30
print("----------------------------------------------------")

#types of function
1)no parameters no return value
2)parameters no return value
3)no parametrs return value
4)parametrs nad return value
'''
def fun1():#no parameters no return value
    a=10
    b=20
    c=a+b
    print(c)

def fun2():#parameters no return value
    a=10
    b=20
    c=a+b
    return c
def fun3(a,b):#no parametrs return value
    c=a+b
    print(c)
def fun4(a,b):#parametrs nad return value
    c=a+b
    return c
fun1()
r1=fun2()
print(r1)
x=10
y=20
fun3(x,y)
r2=fun4(x,y)
print(r2)