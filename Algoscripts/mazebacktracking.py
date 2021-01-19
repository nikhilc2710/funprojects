import collections
from colorama import init
init(autoreset=True)
from colorama import Fore, Back, Style
# print(Back.RED + 'and with a green background')
def wall():
    return Back.RED+'0'

def walk():
    return Back.GREEN+'1'

def goal():
    return Back.BLUE+'G'

def start():
    return Back.CYAN+'S'


# wall, clear, goal = 0, 1, 9
# width,height=map(int,input().split())
# def bfs(grid, start):
#     queue = collections.deque()
#     queue.append(start)
#     seen = set([start])
#     while queue:
#         path = queue.popleft()
#         x, y = path
#         if grid[y][x] == goal:
#             return 1
#         for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
#             if ( 0 <= x2 < width and  #X-axis in range
#                 0 <= y2 < height and  #y-axis
#                 grid[y2][x2] != wall and  #not a wall
#                 (x2, y2) not in seen): #not visited
#                 queue.append( (x2, y2))
#                 seen.add((x2, y2))
#     return 0
mapper={1:walk(),0:wall(),9:goal(),7:start()}
mat=[list(map(int,input().split())) for i in range(8)]
for row in range(8):
    print(' '.join([mapper[i] for  i in mat[row]]))
# print(f'{} {} {} {} {} {} {} {}')
# print(f'{} {} {} {} {} {} {} {}')
# print(f'{} {} {} {} {} {} {} {}')
# print(f'{} {} {} {} {} {} {} {}')
# print(f'{} {} {} {} {} {} {} {}')
# print(f'{} {} {} {} {} {} {} {}')
# print(f'{} {} {} {} {} {} {} {}')
# ans = 0 if mat[0][0]==0 else bfs(mat,(0,0))
# print(ans)

# 1 0 1 1 1 0 0 1
# 1 0 0 0 1 1 1 1
# 1 0 0 0 0 0 0 0
# 1 0 1 0 9 0 1 1
# 1 1 1 0 1 0 0 1
# 1 0 1 0 1 1 0 1
# 1 0 0 0 0 1 0 1
# 1 1 1 1 1 1 1 1