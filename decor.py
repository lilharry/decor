import time

def name(f):
    def inner(*arg):
        return f.func_name + ": " + str(arg)
    return inner

def timer(f):
    t1 = time.time()
    def inner(*arg):
        f(*arg)
        return "execution time: " + str(time.time() - t1) + " secs"
    return inner

@name
def test(x):
    for i in range(x):
        pass

@timer
def test2(x):
    for i in range(x):
        pass
    
#returns nth fib number
@name
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
'''    
y = timer(test)
print test(100000)
print test2(100000)
'''

print fib(5)
