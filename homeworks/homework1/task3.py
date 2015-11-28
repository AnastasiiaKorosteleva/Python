__author__ = 'anastasiiakorosteleva'
a = [1, 2, 3, 4, 5, 6, 7, 8]
i = 0
for j in range(len(a)-1):
    for i in range(len(a)-2):
        if (i%2) == 0:
            if a[i] > a[i+2]:
                c = a[i]
                a[i] = a[i+2]
                a[i+2] = c
        if (i+1)%2 == 0:
            if a[i] < a[i+2]:
                c = a [i]
                a[i] = a[i+2]
                a[i+2] = c
#print(' '.join(map(str, a)))
print(a)

def devide(lst, devision):
    parts = len(lst) // devision
    z = [lst[i:i+parts] for i in range(0, len(lst), parts)]
    return z
    a = z[0]
    b = z[1]
    for i in range(len(a - 1)):
        for j in range(len(b - 1)):
            if a[i] + b[j] == 10:
                return True


print(devide(a, 2))



