__author__ = 'anastasiiakorosteleva'
import sys
data = sys.stdin.read()
import re
pattern = "\W+"
ids = re.sub(pattern, ' ', data)
print(ids)