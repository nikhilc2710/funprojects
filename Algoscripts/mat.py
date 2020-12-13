a=[[1,1,1,1,1,1],
[1,1,0,0,0,0],
[0,0,0,1,1,1],
[0,0,0,1,1,1],
[0,0,1,0,0,0],
[1,0,0,0,0,0],
[1,1,1,1,1,1],
[1,1,1,1,1,1]]
count=0
check=1
arrx=[]
arr=a.__iter__()
for i,j in enumerate(arr):
    while all(j):arrx.append(i);break
print(arrx)
# while set()
# for i in a:
#     while 1 in set(i) and len(set(i))==1:
#          linearrows+=1
#          inndex,val=enumerate
#          break
        
# print(linearrows)
# for i in range(len(a)):
#     index=set((index1,index2) for index1,value1 in enumerate(a) for index2,value2 in enumerate(value1) if value2==check) 
#     if len(index)!=len(a)**2:
#         for x,y in index:
#             l,r,u,d=y-1,y+1,x-1,x+1
#             if u >=0:
#                 a[u][y]=1
#             if d < len(a):
#                 a[d][y]=1
#             if l>=0:
#                 a[x][l]=1
#             if r<len(a):
#                 a[x][r]=1
#     else:
#         break
#     # print(*a,sep="\n")
#     # print('')
#     count+=1
