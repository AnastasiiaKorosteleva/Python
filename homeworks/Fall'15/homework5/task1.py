__author__ = 'anastasiiakorosteleva'
import sys
data = sys.stdin.read()
import re
results = len(re.findall("(Y|y)ou", data))
print(results)