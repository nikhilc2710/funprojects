from collections import deque
def BFS(graph,start,end):
    visited=set()
    q=deque()
    q.append([start,[start]])
    while q:
        n,path=q.popleft()
        visited.add(n)
        for i in graph[n]:
            if i == end:
                return path+[end]
            else:
                if i not in visited:
                    visited.add(i)
                    q.append(i)

graph={
    'A' : ['B','C','D'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : ['A'],
  'E' : ['F'],
  'F' : []
}
print(BFS(graph,'A','D'))