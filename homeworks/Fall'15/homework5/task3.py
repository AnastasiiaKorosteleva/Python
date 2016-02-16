__author__ = 'anastasiiakorosteleva'
import sys
data = sys.stdin.read().split("\n")
import re
string = 0
for i in data:
    ids = re.findall("(\w+) = ", i)
    string += 1
    if len(ids) > 0:
        print(string, ids[0])



