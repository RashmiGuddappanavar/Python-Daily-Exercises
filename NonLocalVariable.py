def fun1():
    a = 10 # Non-Local Variable
    print("From fun1 a ",a)
    def fun2():
        nonlocal a
        a = 100
        b = 20 # Local variable
        print("From fun2 a ", a)
        print("From fun2 b ",b)
    fun2()
    print("From fun1 a ", a)
fun1()        