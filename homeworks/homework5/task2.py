__author__ = 'anastasiiakorosteleva'
import re
import sys

data = sys.stdin.read()
phones = data.split("\n")

for i in phones:
    result = re.findall("0{3}|1{3}|2{3}|3{3}|4{3}|5{3}|6{3}|7{3}|8{3}|9{3}", phones)
    if result == True:
        print(phones)