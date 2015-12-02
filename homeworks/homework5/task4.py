__author__ = 'anastasiiakorosteleva'
import sys
data = sys.stdin.read().split("\n")
import re
string = 0
for i in data:
    sharp = i.lstrip()
    if sharp.startswith('#'):
        string += 1
    else:
        ids = re.findall(' *([\w,. ]+) = ', i)
        string += 1
        if len(ids) > 0:
            print(string, ''.join(ids[0].split(',')))




