def dfs_iterative(graph, start):
    stack, visited = [start], []

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.append(node)
        for n in graph[node]:
            stack.append(n)

    return visited



graph={
    "A":['B','C'],
    "B":['D','E'],
    "C":['F'],
    "D":[],
    "E":['F'],
    "F":[]
    }
print(dfs_iterative(graph,'A'))