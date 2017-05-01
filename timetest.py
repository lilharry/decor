import time

def timer(f):
    t1 = time.time()
    def inner(*arg):
        value = f(*arg)
        print "execution time: " + str(time.time() - t1) + " secs"
        return value
    return inner

    
#returns nth fib number
@timer
def loopNTimes(x):
    for i in range(x):
        pass
        

print loopNTimes(10000000)