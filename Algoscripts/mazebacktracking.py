import collections
wall, clear, goal = 0, 1, 9
width,height=map(int,input().split())
def bfs(grid, start):
    queue = collections.deque()
    queue.append(start)
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path
        if grid[y][x] == goal:
            return 1
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if ( 0 <= x2 < width and  #X-axis in range
                0 <= y2 < height and  #y-axis
                grid[y2][x2] != wall and  #not a wall
                (x2, y2) not in seen): #not visited
                queue.append( (x2, y2))
                seen.add((x2, y2))
    return 0

mat=[list(map(int,input().split())) for i in range(width)]
ans = 0 if mat[0][0]==0 else bfs(mat,(0,0))
print(ans)
