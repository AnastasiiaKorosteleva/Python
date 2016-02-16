__author__ = 'anastasiiakorosteleva'
def plural(n, cases):
    if n % 10 == 1 and n % 100 != 11:
        return cases[0]
    elif 2 <= n % 10 <= 4 and (12 > n % 100 or n % 100 > 14):
        return cases[1]
    else:
        return cases[2]

cases = {"утюг": ["утюг", "утюга", "утюгов"],
         "ложка": ["ложка", "ложки", "ложек"],
         "гармошка": ["гармошка", "гармошки", "гармошек"],
         "чайник": ["чайник", "чайника", "чайников"]}
word = input()
quantity = int(input())
#print(" ".join((str(quantity), plural(quantity, cases[word]))))
print( quantity, plural(quantity, cases[word]))