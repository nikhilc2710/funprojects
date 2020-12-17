from collections import deque
def BFS(graph,node):
    visited=set()
    q=deque()
    q.append(node)
    while q:
        n=q.popleft()
        print(n,end=" ")

        for i in graph[n]:
            if i not in visited:
                visited.add(i)
                q.append(i)

graph={
    'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : ['A'],
  'E' : ['F'],
  'F' : []
}
BFS(graph,'B')