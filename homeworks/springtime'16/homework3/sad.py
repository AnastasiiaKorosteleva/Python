__author__ = 'anastasiiakorosteleva'
#!/usr/bin/python3.3
import argparse
import os.path
import subprocess
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("command", choices=['store', 'diff'],
                    type=str,
                    help="'store' -- saves current state, "
                         "'diff' -- show difference between current and earlier state ")
parser.add_argument("path",
                    type=str,
                    help="Path to the file or directory ")

args = parser.parse_args()
path = args.path

save_here = '/Users/anastasiiakorosteleva/PycharmProjects/Python/sad'
name = path.split('/')[-1]
paste_here = '/Users/anastasiiakorosteleva/PycharmProjects/Python/sad/' + name
if args.command == 'store':
    if os.path.isdir(path):
        print('This is a folder! Please choose a file next time')
    else:
        shutil.copy(path, save_here)
        print("I did store")
elif args.command == 'diff':
    subprocess.call(' '.join(['FC ', path, paste_here]), shell=True)
    print("I did diff")