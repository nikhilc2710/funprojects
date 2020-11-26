# def solve(a,balance):
#     house_Can_buy=0
#     for i in a:
#         if i<=balance:
#             house_Can_buy+=1
#             balance-=i
#     return house_Can_buy
# def main():
#     a=int(input())
#     res=[]
#     for i in range(a):
#         _,balance=list(map(int,input().split()))
#         arr2=list(map(int,input().split()))
#         result=solve(arr2,balance)
#         res.append(result)
#     for i,j in enumerate (res):
#         print("Case #{}: {}".format(i+1,j))
# main()
# import sys
# from collections import defaultdict
# from math import gcd

# def input(): return sys.stdin.readline()

# K = 1_000_000_000
# L = K**2
# print(L)
# D = defaultdict(int)
# for _ in range(int(input())):
#     D[gcd(round(float(input()) * K), L)] += 1
#     print(D)

# D = tuple(D.items())
# ans = 0
# for i, (k1, v1) in enumerate(D):
#     if k1*k1 % L == 0:
#         ans += v1*(v1-1) // 2
#     for k2, v2 in D[i+1:]:
#         if k1*k2 % L == 0:
#             ans += v1 * v2
# print(ans)
#number increment in matrix run code block
a=[ord(i) for i in 'abc']
print(a)
for i in range(len(a)):
    a[i]+=1
    for j in range(i):
        a[j]+=1
        print(a)
#number of pairs sum upto even numbers        
N, M = map(int, input().split())
print(N*(N-1)//2 + M*(M-1)//2)