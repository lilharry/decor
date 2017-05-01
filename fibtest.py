import time

def name(f):
    def inner(*arg):
        print f.func_name + ": " + str(arg)
        return f(*arg)
    return inner


    
#returns nth fib number
@name
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    

print fib(10)

