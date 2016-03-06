__author__ = 'anastasiiakorosteleva'
class A:
    pass
class B:
    pass
class C:
    pass
class D(A,C):
    pass
# import sys
inh = []
for i in A, B, C:
    if issubclass(D, i):
        inh.append(str(i)[-3])
# inh.sort()
print(" ".join(inh))
