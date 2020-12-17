from collections import deque
def BFS(graph,node):
    visited=set()
    q=deque()
    q.append(node)
    while q:
        n=q.popleft()
        if n not in visited:
            visited.add(n)
            print(n,end=" ")

        for i in graph[n]:
            q.append(i)

graph={
    'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}
BFS(graph,'F')