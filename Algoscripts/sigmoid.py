from collections import Counter
def main():
    t=int(input())
    for i in range(t):
        s=input()
        c=Counter(s)
        printed=set()  
        for i in s:
            if i not in printed:
                print(i,c[i])
                printed.add(i)
# main()


def main():
    tt=int(input())
    for i in range(tt):
        n=int(input())
        arr=tuple(map(int,input().split()))
        k=int(input())
        ans=[i for i in arr if i!=k]
        temp=[1]*(n-len(ans))
        ans=temp+ans
        print(ans)
# main()
matrix =matrix = [
    ["#", "#"],
    [".", "#"]
]
# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
clockwise90=[list(i[::-1]) for i in zip(*matrix)]

hash_count=0
R,C=len(clockwise90),len(clockwise90[0])
print(*clockwise90,sep="\n")
print("~~~~~~~~~~~~~~~~~~~~~~")
for col in range(C):
    for row in range(R):
        if clockwise90[row][col]=='#':
            clockwise90[row][col]="."
            hash_count+=1
        elif clockwise90[row][col]=='*' :
            print(hash_count)
            temp=row-1
            while temp>-1 and hash_count:
                temp= temp if temp >-1 else 0
                clockwise90[temp][col]='#'
                print((row,col))
                hash_count-=1
                temp-=1
        elif row==R-1 and clockwise90[row][col]=='.':
            temp=row
            while temp>0 and hash_count:
                temp=temp if temp >0 else 0
                clockwise90[temp][col]='#'
                hash_count-=1
                temp-=1
    hash_count=0
print(*clockwise90,sep="\n")

from itertools import accumulate
def prefix(arr):
    print(arr)
    arr=list(accumulate(arr,initial=0))
    #0-3
    print(arr)
    print(arr[6]-arr[2])
    #print(arr)

prefix([1,2,5,0,3,7])
