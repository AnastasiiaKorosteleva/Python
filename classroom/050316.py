__author__ = 'anastasiiakorosteleva'
import subprocess
import os
# subprocess.call("ls")
file_names = []
for description in os.walk("."):
    prefix, subdir, files = description
    files_with_prefix = [prefix + "/" + x
                         for x in files
                         if  x.endswith(".py")
                         ]
    file_names.extend(files_with_prefix)



# for file in file_names:
#     subprocess.call(["pep8", file])


# for file in file_names:
#     p = subprocess.Popen(["pep8", file], stdout=subprocess.PIPE)
#     stdout, stderr = p.communicate()
#     print(stdout)
code = []
for file in file_names:
    p = subprocess.Popen(["cat", file], stdout=subprocess.PIPE)
    print(p.pid)
    stdout, stderr = p.communicate()
    code.append(stdout.decode("utf-8"))

code = "\n".join(code)
with open("total.py", "w") as f:
    