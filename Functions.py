# Functions - It is blk of code included to perform a specific task 
# - It will be executed only if it is called 
# - Parameters and return val/val's of a function will be decided based on the requirements
# - It is a independent blk of code

# Usage:
#                 - Code optimization
#                 - Readability
#                 - Code Reusability

# Syntax: 
#                  def function_name(parameters):
                    # logic
                    #  return val or val's

#                  var_name = function_name(arguments)
#                  #then reuse the returned val

# Controlflow of functions

# called function
def addnum(n1, n2): #Function declaration
    sum = n1 + n2 #-----|
    return sum    #-----| Function defination

res = addnum(10,20) # functioncall
print(res + 5)
print(res - 5)
print(res * 10)

# n1, n2 --> parameters - i/p req by a fun to perform an action , It is a dynamic local variable
# 10 20 --> arguments - the values that are passed to the function
# sum --> return val

# return = it's a keyword, last executed line of code 
# returns from called function to the functioncall

def function1():
    a = 10
    b= 20
    prod = a + b
    print(prod)
    
def function2(a, b):
    prod = a * b
    return prod   

function1()
function1()
function1() 
function1()
function1()
function1()
res = function2(10,20)

# Function declaration - it includes the basic details & requirement of the function
# a. function_name ==> decided based on the task to be performed 
# b. parameters ==> The input's required by a function to perform 
#                   a. specific task
#                      - They are dynamic local variables
# 
# Function defination ==> 
#                   - the logic associated to a specific task 
#                   - "return"
#                            - basically a keyword
#                              last executable line of code in a function, once "return" is executed in a function, no other line of code, included in the function would work
#                   Uses:
#                             - it helps to return one or multiple val's from called function back to function call, tht can be reused in further program 
#                             - it returns back the execution flow of PVM from called function back to function call  