from bisect import bisect_left
import sys
def input():
    return sys.stdin.readline().strip()
def digit():
    return int(input())
def listip():
    return list(map(int,input().split()))

def mybin(a,l,r,t):
    while l<=r:
        mid=l+(r-l)//2
        if a[mid]==t:
            return 'YES'
        if a[mid]<=t:
            l=mid+1
        else:
            r=mid-1
    return 'NO'
def main():
    a,b=listip()
    a1,b1=listip(),listip()
    
    res=[]
    for i in range(len(b1)):
        res.append(mybin(a1,0,len(a1)-1,b1[i]))
    print(*res,sep="\n")
main()

#Cube sorting
"""
idea given (n(n-1)/2)-1
a array can have maximum (n(n-1)/2) pairs
the condition will only acepted if aray in in descending order  as there will be nothinh to swaped
check codnotes youtube video
"""
from random import randint
tt=int(input())
for _ in range(tt):
    n=int(input())
    a=list(map(int,input().split()))
    ans='NO'
    for i in range(len(a)-1):
        if not a[i]>a[i+1]:
            ans='YES'
            break
    print(ans)
# Longest palnidromic subsequence
#get max element from string and count occurences of that eleemnt
s = input()
k = max(s)
ans = k*s.count(k)
print (ans)



