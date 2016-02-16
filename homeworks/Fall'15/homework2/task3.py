__author__ = 'anastasiiakorosteleva'
def euclid(a, b):
    return a if b == 0 else euclid(b, a % b)
lst =  ([int(i) for i in input().split()])
print(euclid(lst[0], lst[1]))