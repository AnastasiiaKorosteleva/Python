__author__ = 'anastasiiakorosteleva'
import sys
data = sys.stdin.read().split("\n")
import re
for index,i in enumerate(data):
    sharp = i.lstrip()
    if sharp.startswith('#'):
        continue
    else:
        ids = re.findall(' *([\w,. ]+) = ', i)
        if len(ids) > 0:
            print(index+1, ''.join(ids[0].split(',')))




