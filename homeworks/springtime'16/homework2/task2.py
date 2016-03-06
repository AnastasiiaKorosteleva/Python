__author__ = 'anastasiiakorosteleva'

def recursive(node):
    if node not in visited:
        visited.append(node)
        if node in classes:
            for i in classes[node]:
                recursive(i)
    else:
        return

n = int(input())
classes = {}
for i in range(n):
    first, *second = input().split(" : ")
    if second != []:
        second = second[0].split(" ")
    if first not in classes:
        classes[first] = second
    else:
        classes[first].append(second)
q = int(input())
query_list = list()

for i in range(q):
    query_list.append(input())
for i in query_list:
    visited = []
    second, first = i.split(' ')
    recursive(first)
    if second in visited:
        print("Yes")
    else:
        print("No")

# def dfs(graph, start):
#     visited, stack = set(), [start]
#     while stack:
#         vertex = stack.pop()
#         if vertex not in visited:
#             visited.add(vertex)
#             stack.extend(graph[vertex] - visited)
#     return visited