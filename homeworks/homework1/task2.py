__author__ = 'anastasiiakorosteleva'
a=[int(i) for i in input().split()]
s=0
c=0
b = len(a)
for i in range(b):
    s+=a[i]
    c = c+1
print(s/c)