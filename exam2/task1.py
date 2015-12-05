__author__ = 'anastasiiakorosteleva'
import re
input_file = open('hp5.txt', 'r')
sentences = input_file.read().split('.')
library = {}
for sentence in sentences:
     m = re.findall(r'whispered ([A-Z][a-z]+( [A-Z]\w+)*)|([A-Z][a-z]+( [A-Z]\w+)*) whispered', sentence)
     if m:
        all = list(m)
        for group in all:
            tmp = ' '
        for person in group:
            if len(tmp) < len(person):
                tmp = person
            if tmp not in library:
                library[tmp] = 1
            else:
                library[tmp] += 1
score = (0, 0)
for i in library:
    if score[0] < library[i]:
        score = (library[i], i)
print(score[0], score[1])
