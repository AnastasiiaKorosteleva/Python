__author__ = 'anastasiiakorosteleva'

quantity = int(input())
functions = input().split()
m = int(input())
except_list = []

for k in range(m):
    except_list.append(input())

except_dict = {}
last_except = input()

for i in except_list:
    key = i.split()
    if key[0] not in except_dict:
        except_dict[key[0]] = {key[1]: key[2]}
    else:
        except_dict[key[0]].update({key[1]: key[2]})


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

