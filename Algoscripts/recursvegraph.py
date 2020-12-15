visited=set()
def recursiveDFS(graph,node,visited):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
    for n in graph[node]:
        DFS(graph,n,visited)


graph={
    "A":['B','C'],
    "B":['D','E'],
    "C":['F'],
    "D":[],
    "E":['F'],
    "F":[]
    }
DFS(graph,'A',visited)