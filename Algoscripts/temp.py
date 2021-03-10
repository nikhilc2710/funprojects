from numpy import searchsorted
from numpy import array
from numpy import concatenate

def solve(Queryies,mat):
    sumRowCol=concatenate([ mat.sum(axis=1),mat.sum(axis=0)])
    sumRowCol.sort()
    ans=[searchsorted(sumRowCol,right,'right')-searchsorted(sumRowCol,left,'left') for left,right in Queryies]
    # for i in Queryies:
    #     left,right=i
    #     leftcount=searchsorted(sumRowCol,left,'left')
    #     rightcount=searchsorted(sumRowCol,right,'right')
    #     ans.append(rightcount-leftcount)
    print(" ".join(map(str,ans)))

    
def main():
    R=int(input())
    C=int(input())
    if not R or not C:return 0
    mat=array([[int(i) for i in input().split()] for i in range(R)])
    Q=int(input())
    _=int(input())
    Queryies=[]
    for i in range(Q):
        Queryies.append([int(i) for i in input().split()])
    solve(Queryies,mat)
main()
