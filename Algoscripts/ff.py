# noofelem,noq=list(map(int,input().split()))
# a=list(map(int,input().split()))
# res=[]
# lookup={}
# for i in range(noq):
#     l,r,p,k=list(map(int,input().split()))
#     subarray=a[l-1:r]
#     print(subarray)
#     xr=0
#     for i in range(p):
#         for index,x in  enumerate(subarray):
#             xr^=x+k
#             if x in lookup:
#                 subarray[index]=lookup[x]
#             else:
#                 subarray[index]//=2
#                 lookup[x]=subarray[index]//2
#     res.append('EVEN' if xr%2==0 else 'ODD')
# print(*res,sep="\n")


# import math
# def solve(n,k,MOD):
#     return math.comb(n,k)%MOD
# MOD=1000000007
# MOD=1000000007
# print(10**9+7)
# print(solve(10000,555,MOD))
