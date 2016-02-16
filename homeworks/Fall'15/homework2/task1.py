__author__ = 'anastasiiakorosteleva'
def factorial(x):
    a = 1
    i = 1
    for i in range(1, x+1):
        a = a*i
    return(a)

def combinations(n,k):
    if k > n:
        y = 0
    elif k == n or k == 0:
        y = 1
    else:
        y = factorial(n)/(factorial(k)*factorial(n - k))
    return int(y)


a = ([int(i) for i in input().split()])
print(combinations(a[0], a[1]))