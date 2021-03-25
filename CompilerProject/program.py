a,b=map(int,input().split())
temp=[]
for row in range(a):
    temp.append(list(input().split()))
q=int(input())
x=[]
for i in range(q):
    x.append(input().split())

print(temp,x)
