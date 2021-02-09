# a=[-10,0,11]
# ans=9999
# for  i in range(1,len(a)):
#     ans=min(ans,abs(a[i-1]-a[i]))
# print(ans)
# def tenpercent(n):
# 	return (n*10)/100
# def fivepercent(n):
# 	return (n*5)/100
# def twentpercnet(n):
# 	return (n*20)/100

# a=[20,10,30,9,80,100]
# b=[2,1,2,2,3,1]
# ans=0
# for i,item,q in zip(range(1,len(a)+1),a,b):

# 	if i<=2:
# 		if item>10:
# 			ans+=q*tenpercent(item)
# 	else:
# 		if item>60:
# 			ans+=q*twentpercnet(item)
# 		elif item>10:
# 			ans+=q*fivepercent(item)

# print(round(ans))

# letters={}
# M=6
# arr=[[i for i in input()] for i in range(M)]
# N=len(arr[0])
# for row in range(M):
# 	for col in range(N):
# 		letters[arr[row][col]]=0
# def dfs(row,col,char):
# 	arr[row][col]='visited'
# 	for x,y in (1,0),(0,1),(-1,0),(0,-1):
# 		currx,curry=row+x,col+y
# 		if 0<=currx<M and 0<=curry<N and arr[currx][curry]==char:
# 			dfs(currx,curry,char)

# for i in letters:
# 	for row in range(M):
# 		for col in range(N):
# 			if arr[row][col]==i:
# 				dfs(row,col,i)
# 				letters[i]+=1
# print(letters)

# a={'a': 2, 'b': 3, 'x': 1, 'd': 1}
# x=[(k,v) for k,v in a.items()]
# x.sort(key=lambda  x: (x[1],-ord(x[0])),reverse=True)
# print(x)
# print(sorted(a.items(),key=lambda  x: (x[1],-ord(x[0])),reverse=True))


# # A Python program to find the first, 
# # second and third minimum element  

  
# def Print3Smallest(number, n): 
#     if len(number)<2:
#         return []
#     firstmin = float('inf')
#     secmin = float('inf')
#     thirdmin = float('inf')
  
#     for i in range(len(number)): 
          
  
#         if arr[i] < firstmin: 
#             thirdmin = secmin 
#             secmin = firstmin 
#             firstmin = arr[i] 
  

#         elif arr[i] < secmin: 
#             thirdmin = secmin 
#             secmin = arr[i] 

#         elif arr[i] < thirdmin: 
#             thirdmin = arr[i] 
#     return [secmin,thirdmin]
  
  
# # driver program 
# arr = [2] 
# n = len(arr) 
# print(Print3Smallest(arr, n)) 
from itertools import groupby
from math import log10
arr=[101,317,332,62,1226,631,865,539,62,9,333,222,555,666,777,889,998]
test=[int(log10(i))+1 for i in arr]
xx=groupby(enumerate(test),lambda x:x[1])
l = [ list(x[1]) for x in xx if x[0] == 3]
for i in reversed(l):
	left,right=i[0][0],i[-1][0]
	arr[left:right+1]=[max(arr[left:right+1])]
print(arr)