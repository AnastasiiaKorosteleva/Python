__author__ = 'anastasiiakorosteleva'
n = int(input())
class_list = list()
for k in range(n):
    class_list.append(input())
q = int(input())
query_list = list()
for l in range(q):
    query_list.append(input())



print(class_list)
print(query_list)
print(query_list[0])



# class_dict = {}
#
for i in class_list:
    if ":" in i:
        if i[0] not in class_dict:
            if len(i) <= 5:
                class_dict[i[0]] = i[4]
                # print(class_dict)
            if len(i) > 5:
                class_dict.setdefault(i[0],[i[4]]).append(i[6])
print(class_dict)
query_dict = {}
for i in query_list:
    query_dict[i.split()[0]] = i.split()[1]
#     inv_d = {v:k for k, v in query_dict.items()}
# print(inv_d)
print(query_dict)

# list_que_val = list(query_dict.values())
# list_que_keys = list(query_dict.keys())
# list_classdict_val = list(class_dict.values())
# # list_classdict_key = list(class_dict.keys())
# print(list_que_val)
# print(list_que_keys)

# for i in query_dict.keys():
#     for j in class_dict.values():
#         if i == j:
#             print("ya")
