# import sys
# tt=int(input())
# for i in range(tt):
#     ip=list(map(int,sys.stdin.readline().strip().split()))
#     map_={v:chr(i+65) for i,v in enumerate(ip)}
#     print(map_)
#     map_['Y']=4
#     target=int(input())
#     max_=max(map_.keys())
#     res=""
#     want,_=divmod(target,map_[max_])
#     res=max_*want
#     nexchar=target-(map_[max_]*want)
#     temp=""
#     for i in map_:
#         if map_[i]==nexchar:
#             temp=max(temp,i)
#     print(res+temp)
# from operator import xor
# from functools import lru_cache
# from functools import reduce
# import sys
# def helper(z): 
#     n=len(z)
#     cost = sys.maxsize
#     XOR =reduce(xor,z)
#     for i in range(0,n): 
#         if (cost > abs((XOR ^ z[i]) - z[i])): 
#             cost = (XOR ^ z[i]) -z[i] 
#             element = i
#     return [element, cost]
# #[7, 29, 26, 16, 8,7,16,16,24,24,7,16,24,24,0,7,16,16]
# arr=[7, 29, 26, 16, 8,7]
# print(len(arr))
# count=0
# zz=0
# for i in range(len(arr)-5+1):
#     index,value=helper(arr[i:5+i])
#     if value!=0 and index+i>=i:
#         count+=1
#         arr[index+i]+=value
# print(count)

# 2
# 3
# 1 2 2
# 4
# 1 2 3 2
# import sys
# def input():
#     return sys.stdin.readline().strip()
# tt=int(input())
# for i in range(tt):
#     people,limit=map(int,input().split())
#     arr=list(map(int,input().split()))

# 2
# 3 3
# 2 7 4
# 5 6
# 9 10 4 7 2
# a=[3,4,-1,1]
# a.append(0)
# N=len(a)
# for i in range(N):
#     if a[i]<0 or a[i]>N:
#         a[i]=0
# for i in range(N):
#     if a[i]>0:
#         a[a[i]%N-1]+=N
# print('A after mod operation',a)
# for i in range(N):
#     if a[i]//N==0:
#         print(a[i])
#         print(i+1)
#         exit()
#find pairs whose sum uptko k
# nums = [1,3,1,5,4]
# k = 0
# from collections import Counter
# count=Counter(nums)
# if k>0:
#     res=[i+k in count for i in count]
# else:
#     res=[count[i]>1 for i in count]
# print(res)
######################################################
# import sys
# import random
# from fractions import Fraction
# from math import *
 
# def input():
#     return sys.stdin.readline().strip()
 
# def iinput():
#     return int(input())

# def finput():
#     return float(input())

# def tinput():
#     return input().split()

# def linput():
#     return list(input())
 
# def rinput():
#     return map(int, tinput())

# def fiinput():
#     return map(float, tinput())
 
# def rlinput():
#     return list(map(int, input().split()))
# def trinput():
#     return tuple(rinput())

# def srlinput():
#     return sorted(list(map(int, input().split())))

# def NOYES(fl):
#     if fl:
#         print("NO")
#     else:
#         print("YES")
# def YESNO(fl):
#     if fl:
#         print("YES")
#     else:
#         print("NO")
    
# def main():
#     n = iinput()
#     #k = iinput() 
#     #m = iinput() 
#     #n = int(sys.stdin.readline().strip()) 
#     #n, k = rinput()
#     #n, m = rinput()
#     #m, k = rinput()
#     #n, k, m = rinput()
#     #n, m, k = rinput()
#     #k, n, m = rinput()
#     #k, m, n = rinput() 
#     #m, k, n = rinput()
#     #m, n, k = rinput()
#     #q = srlinput()
#     #q = linput()
#     q = [(int(i) + v) % 2 for v, i in enumerate(list(input()))]
#     print(q)
#     print(1 + (n % 2) * (sum(q[0: :2]) == 0) + ((n + 1) % 2) * (sum(q[1: :2]) != 0),'Where are you')

# for i in range(iinput()):
# #     main()
# N=int(input())
# target=N+1
# jumpsallowed=int(input())
# jumpdistance=int(input())
# pos=[int(input()) for i in range(jumpsallowed)]
# pos.insert(0,0)
# hash=set(pos)
# maxpossjump=0
# for index,i in enumerate(pos):
#     maxpossjump=i+jumpdistance
#     for x in range(maxpossjump,-1,-1):
#         if x in hash:
# #             jumpsallowed-=1
# #  
# #           break   
# import sys
# # def input():
# #     return sys.stdin.readline().rstrip()

# s,count=map(int,input().split())
# arr=list(map(int,input().split()))
# temp=[arr[i:i+count] for i in range(s-count+1)]
# print(temp)
# ans=[]
# for i in temp:
#     if i[0]<0:
#             ans.append(i[0])
#     else:
#         ans.append(0)
            
# print(ans)
def solve(tt):
    if tt=='t1':
        n,g=6,3
        x=[]
        arr=[-11,-2,19,37,64,-18]
        #arr=[35, -42 ,23 ,-56 ,-84 ,92 ,39]
        print([[i+1,(i+1)+3] for i,j in enumerate(arr) if j<0])
        # arr+=[0]*g
        # arr=[arr[i:i+g] for i in range(n)]
        # print(arr)
        # m=9999
        # temp=[]
        # flag=False
        # for index,i in enumerate(arr):
        #     if i[0]<0:
        #         x.append(i[0])
        #         flag=False
        #     else:
        #         if not flag:
        #             x.append(0)
        #             flag=True
    # print(temp)
    # print(x)
            

solve('t1')




