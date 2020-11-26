n=int(input())
li=list(map(int,input().split()))
li.sort()
s=sum(li)
def minimum(s,li):
    if(len(li)==1):
        return abs(s-2*li[0])
    else:
        m=abs(s-2*li[0])
        for i in range(1,len(li)):
            m=min(m,abs(minimum(s-2*li[i],li[:i])))
        return m
print(minimum(s,li))