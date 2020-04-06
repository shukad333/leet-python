import math

def isPerfectSquare(x):
    s = int(math.sqrt(x))
    A=[]
    A.sort()
    return s*s == x

def isFibonacci(n):
    return isPerfectSquare(5*n*n-4) or isPerfectSquare(5*n*n+4)

for i in range(1,11):
    if(isFibonacci(i)):
        print(i,"is fib")