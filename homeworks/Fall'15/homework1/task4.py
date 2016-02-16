__author__ = 'anastasiiakorosteleva'

ext = input()
indecies = set(text)
values = (text.count(letter) for letter in indecies)
analize = dict(zip(indecies, values))
b = analize.keys()
b = list(b)
b.sort()
for key in b:
    print(key +' '+ str(analize[key]))