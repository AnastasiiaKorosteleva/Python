__author__ = 'anastasiiakorosteleva'

#!/usr/bin/python3.3
import subprocess
import re
import argparse
import os.path


parser = argparse.ArgumentParser(description="We can make picture 100*100!")

parser.add_argument("-path",
                    type=str,
                    help="Path to  file or directory")
parser.add_argument("-new_path",
                    type=str,
                    help="path to converted files")
args = parser.parse_args()
path = args.path
new_path = args.new_path

if not os.path.exists(path):
    print("Don't find file or dir")
else:
    if os.path.isfile(path):
        if new_path is None:
            new_path = path
        com = "convert "+path+" -resize 100x100! "+new_path
        subprocess.call(com, shell=True)
    else:
        for d, dirs, files in os.walk(path):
            for f in files:
                path = os.path.join(d, f)
                a = re.findall("\.png", path)
                b = re.findall("\.jpg", path)
                if a != [] or b != []:
                    com = "convert "+path+" -resize 100x100! "+path
                    subprocess.call(com, shell=True)