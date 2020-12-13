# def dfs_iterative(graph, start):
#     stack, path = [start], []

#     while stack:
#         vertex = stack.pop()
#         if vertex in path:
#             continue
#         path.append(vertex)
#         for neighbor in graph[vertex]:
#             stack.append(neighbor)

#     return path


# adjacency_matrix = {1: [3], 2: [3],
#                     3: [1,2]}