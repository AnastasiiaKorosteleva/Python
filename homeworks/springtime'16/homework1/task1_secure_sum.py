__author__ = 'anastasiiakorosteleva'

def sum(a,b):
    if (a<0 or b<0) and (type(a) is int and type(b) is int):
        raise ValueError()
    elif (type(a) is int and type(b) is int):
        return a + b
    else:
        raise TypeError()


try:
    sum(5,"sds")
except (TypeError, ValueError) as err:
    print("caught", )
