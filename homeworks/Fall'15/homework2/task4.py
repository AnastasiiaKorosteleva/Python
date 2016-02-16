__author__ = 'anastasiiakorosteleva'
def euclid(a, b):
    return a if b == 0 else euclid(b, a % b)

def rpfilter(a, *args):
    lst =  args
    new_lst = []

    for i in range(0,(len(lst)), 1):
        if euclid(a,lst[i]) == 1:
            new_lst.append(lst[i])
    return new_lst

a = ([int(i) for i in input().split()])
b = a.pop(0)
if rpfilter(b, *a) != []:
    print(' '.join(map(str, rpfilter(b, *a))))
else:
    print(None)
