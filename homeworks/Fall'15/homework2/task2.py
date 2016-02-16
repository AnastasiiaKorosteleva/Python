__author__ = 'anastasiiakorosteleva'
import math
def prime(x):
    i = 2
    if x == 0 or x == 1:
        return False
    while 2 <= i <= math.sqrt(x):

        if x % i == 0:
            return False
        i = i+1
    return True

a = int(input())
b = []
for i in range(a):
    c = int(input())
    b.append(c)
for i in range(len(b)):
    print(prime(b[i]))