__author__ = 'anastasiiakorosteleva'
import re
input_file = open('links.txt', 'r')
sentences = input_file.read().split('.')
ids = re.findall(r'[\d\w._]+@[\d\w._]+')