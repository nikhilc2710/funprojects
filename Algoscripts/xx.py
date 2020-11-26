def solve(a):
    mi=mx=0
    length=len(a)
    for i in range(len(a)):
        if a[mi]>=a[i]:
            mi=i
        if a[mx]<a[i]:
            mx=i
    if mi<mx:
        length-=1
        return (length-mi)+(mx-1)
    else:
        return (length-mi)+mx-1
    
def main():
    x=int(input())
    a=list(map(int,input().split()))
    res=solve(a)
    print(res)
main()
# a=
# length=len(a)
# print(length-1)

# mi=mx=0
# for i in range(len(a)):
#     if a[mi]>=a[i]:
#         mi=i
#     if a[mx]<a[i]:
#         mx=i
# print(mi,mx)