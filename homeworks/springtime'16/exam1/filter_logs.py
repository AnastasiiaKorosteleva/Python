#!/usr/bin/python3.3
import argparse
import os.path
import subprocess
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("mode", choices=['W', 'WE'],
                    type=str,
                    help="'W' -- show warnings, "
                         "'WE' -- show warnings and errors ")
parser.add_argument("path",
                    type=str,
                    help="Path to the file or directory ")
parser.add_argument("path2",
                    nargs='?',
                    type=str,
                    help="Path to the file or directory  with result")

args = parser.parse_args()
path = args.path
path2 = args.path2
# save_here = '/Users/anastasiiakorosteleva/PycharmProjects/Python/exam2'
# name = path.split('/')[-1]
# paste_here = '/Users/anastasiiakorosteleva/PycharmProjects/Python/exam2/' + name

if path2:
    if args.mode == 'W':
        if os.path.isfile(path):
            subprocess.call('grep -iE "warn" ' + path + ' > ' + path2, shell=True)

        elif os.path.isdir(path):
            subprocess.call('grep -iEr "warn" ' + path + ' > ' + path2, shell=True)
    elif args.mode == 'WE':
        if os.path.isfile(path):
            subprocess.call('grep -iE "warn|err" ' + path + ' > ' + path2,shell=True)

        elif os.path.isdir(path):
            subprocess.call('grep -iEr "warn|err" ' + path + ' > ' + path2 ,shell=True)


else:
    if args.mode == 'W':
        if os.path.isfile(path):
            subprocess.call('grep -iE "warn" ' + path, shell=True)
        elif os.path.isdir(path):
            subprocess.call('grep -iEr "warn" ' + path, shell=True)
    elif args.mode == 'WE':
        if os.path.isfile(path):
            subprocess.call('grep -iE "warn|err" ' + path,shell=True)
        elif os.path.isdir(path):
            subprocess.call('grep -iEr "warn|err" ' + path,shell=True)





