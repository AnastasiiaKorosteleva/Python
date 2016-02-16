__author__ = 'anastasiiakorosteleva'

def factorial(x):
    a = 1
    i = 1
    for i in range(1, x+1):
        a = a*i
    return(a)

dictionary = open('dict.txt', 'r')
words = dictionary.read().split()
list_of_adj = []
list_of_sub = []
list_of_verb = []
for word in words:
        if word[len(word) - 2:] == 'yo':
            list_of_adj.append(word)
        elif word[len(word) - 2:] == 'ka':
            list_of_sub.append(word)
        else:
            list_of_verb.append(word)

adj_comb = 0
if len(list_of_adj) < 7:
    for i in range(1, len(list_of_adj)+1):
        adj_comb += factorial(len(list_of_adj))/factorial(len(list_of_adj)-i)
else:
    for i in range(1, 8):
        adj_comb += factorial(len(list_of_adj))/factorial(len(list_of_adj)-i)

print(int(adj_comb * len(list_of_sub) * len(list_of_verb)))

dictionary.close()