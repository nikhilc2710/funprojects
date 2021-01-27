import random
from itertools import chain
a=[55,33,65,23,66,78,70,230,10,11,56,78]
a.sort(key=lambda  x: [x%2,x])

def digitize(n):
    ans=0
    while n>0:
        ans+=n%10
        n=n//10
    return ans
# print(digitize(55))

b=a[::-1]
s=""
for i,j in enumerate(zip(a,b)):
    if not i%3 and i>0:
        s+=' '
    s+=''.join(map(str,j))
# print(s)
a=[35, -42, 23 ,-56, -84, 92, 39]
a=[-11 ,-2 ,19 ,37 ,64 ,-18]
temp=[]
k=3

ans=[]
for i in range(len(a)-k+1):
    temp.append(a[i:i+k])

for i in temp:
    Flag=True
    for j in i:
        if j<0:
            Flag=False
            i.append(Flag)
            break

for i in temp:
    if not i[-1]:
        for j in i:
            if j<0:
                ans.append(j)
                break
    else:
        ans.append(0)
        
print(ans)
