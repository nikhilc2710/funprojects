#Kickstart Round D 1 sooktuon
# from itertools import groupby
# def solve(a):
#     previous=[]
#     for i in range(len(a)-1):
#         x=a[i+1]-a[i]
#         previous.append(x)
#     previous=max([len(list(v)) for _,v in groupby(previous)])
#     return previous+1
# def main():
#     a=int(input())
#     result=[]
#     for i in range(a):
#         no_of_element=int(input())
#         arr=list(map(int,input().split()))
#         res=solve(arr)
#         result.append(res)
#     for  i,j in enumerate(result):
#         print("Case #{}: {}".format(i+1,j))
# main()
# s = "abc"
# t = "ahbgdc"
# from collections import defaultdict
# checked=s[0]
# counter=0
# for i in s:
#     if checked in t:
#         counter+=1
#         checked=s[counter]
#         print(checked)
# print(counter)
#Hackerrank partially appcepted simple array query
# import sys
# def input(): return sys.stdin.readline()
# _,noq=list(map(int,input().split()))
# arr=list(map(int,input().split()))
# for i in range(noq):
#     task,i1,i2=list(map(int,input().split()))
#     i1-=1
#     if task==1:
#         arr=arr[i1:i2]+arr[:i1]+arr[i2:]
#     else:
#         arr=arr[:i1]+arr[i2:]+arr[i1:i2]
# print(abs(arr[-1]-arr[0]))
# print(*arr)

#math.gcd
#914. X of a Kind in a Deck of Cards Leetcode
#check gcd of list in case asked atleast x pair possible
# from math import gcd
# class Solution:
#     def hasGroupsSizeX(self, a: List[int]) -> bool:
#         return reduce(gcd,Counter(a).values())>=2
        