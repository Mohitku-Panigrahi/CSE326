# from collections import deque
# #graph
# graph = {
#     'A': ['B','C'],
#     'B': ['D','E'],
#     'C': ['F'],
#     'D':[],
#     'E':[],
#     'F': []
# }
# def bfs(graph,start):
#     visited =set()
#     queue = deque([start])
#     while queue:
#         node = queue.popleft()
#         if node not in visited:
#             print(node,end=" ")
#             visited.add(node)
#             for neighbour in graph[node]:
#                 queue.append(neighbour)
# bfs(graph,'A')

from collections import deque
#graph
graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D':[],
    'E':[],
    'F': []
}
def bfs(graph,start):
    visited =set()
    stack = [start]
    while stack:
        node =stack.pop()
        if node not in visited:
            print(node,end=" ")
            visited.add(node)
            for neighbour in reversed[node]:
                stack.append(neighbour)
bfs(graph,'A')