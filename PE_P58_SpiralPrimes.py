## Author: James Norcross
## Date: 4/28/15
## Description:  Finds the width of integer spiral for which the percentage of
## diagonal elements which are prime is less than 10 percent

from math import sqrt

def isPrime(n):
    if (n == 1):
        return False
    for i in range(2, int(sqrt(n))+1):
        if (n%i == 0):
            return False
    return True
    


layer = 0
ratio = 1
current = 1
width = 1
total = 1
prime = 0

while (ratio >= 0.1):
    
    layer += 1
    width = 2*layer + 1
    delta = width - 1
    
    for i in range (4):
        
        current += delta
        total += 1
        if (isPrime(current)):
            prime += 1

    ratio = float(prime)/total

print "The width at which the ratio of primes on the diagonal is less than 10 percent is %s" % width

