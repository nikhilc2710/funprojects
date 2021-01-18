# 3 4
# 0001
# 0011
# 0110
height,width=map(int,input().split())
from collections import deque
def bfs(mat,start):
    goal=1
    q=deque()
    q.append(start)
    visited=set()
    visited.add(start)
    while q:
        path=q.popleft()
        x,y=path
        if mat[x][y]==goal:
            temp=(x,y)
            return [x,y]

        for x2,y2 in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if (0<=x2<height and
                0<=y2<width and
                (x2,y2) not in visited):
                q.append((x2,y2))
                visited.add((x2,y2)) 

matrix=[list(map(int,input().split())) for i in range(height)]

ans=[[999 for _ in range(width)] for i in range(height)]
for row in range(height):
    for col in range(width):
        if not matrix[row][col]:
            x=bfs(matrix,(row,col))
            if x:
                temp=abs(row-x[0])+abs(col-x[1])
                ans[row][col]=min(ans[row][col],temp)
for row in range(height):
    for col in range(width):
        if ans[row][col]==999:
            ans[row][col]=0
print(ans)
            
            




