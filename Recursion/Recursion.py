def sqr(n):# Tail Recursion
    if n > 0:
        k = n**2
        print(k)
        sqr(n-1)
        
sqr(4)


def sqr(n): # Head recursion
    if n > 0:
        sqr(n-1)
        k = n**2
        print(k)
        
        

sqr(4)

def sqr(n): # Tree recursion
    if n > 0:
        sqr(n-1)
        k = n**2
        print(k)
        sqr(n-1)
        

sqr(3)

# Sum of N Natural Numbers

def sumcalc(n):
    if n == 1:
        return 1
    return sumcalc(n-1) + n
    
sumcalc(5)



# Factorial

def fact(n):
    if n == 0:
        return 1
    return fact(n-1)*n

for ii in range(0,10):
    print(ii, fact(ii))
    
    
# Fibonacci


def Fibonacci(n):
    if n<2:
        return n
    return Fibonacci(n-1) + Fibonacci(n-2)
  
  
for ii in range(0,10):
    print(ii, Fibonacci(ii))
