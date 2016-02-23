__author__ = 'anastasiiakorosteleva'

quantity = int(input())
functions = input().split()
m = int(input())
except_list = []
for i in range(m):
    except_list.append(input())
last_except = input()
except_dict = {}

for i in except_list:
    key = i.split()[0] # function
    if key not in except_dict:
        except_dict[key] = {i.split()[1]: i.split()[2]}
    else:
        except_dict[key[0]].update({i.split()[1]: i.split()[2]})

stack = reversed(functions)

for j in stack:
    if last_except in except_dict[j]:
        value = except_dict[j]
        if value[last_except] == '_':
            break
        else:
            last_except = value[last_except]
            quantity = quantity - 1
    else:
        quantity = quantity - 1
print(' '.join(map(str,functions[0:quantity])))

# for i in range(quantity):
#     print(functions[i])
