import sys
def input():
    return sys.stdin.readline().strip().split()
def digit():
    return int(sys.stdin.readline().strip())
#weired Algorithm
# i=int(input())
# res=[i]+[]
# while i!=1:
#     if i&1==1:
#         i=(i*3)+1
#         res.append(i)
#     else:
#         i=i//2
#         res.append(i)
# print(*res)

# missing Number
# res=int(input())
# a=set(list(map(int,input().split())))
# for i in range(1,res+1):
#     if i not in a:
#         print(i)
#         break
#DNA Securence
# from itertools import groupby
# a=input()
# print( max(len(list(v)) for _,v in groupby(a))) 

#increasing array
# a=int(input())
# arr=list(map(int,input().split()))
# temp,ans=0,0
# for i in arr:
#     temp=max(i,temp)
#     ans+=temp-i
# print(ans)
#beautiful permuations
#approch print even nunmbers first then  odd numbers 
# print(list(chain.from_iterable(zip([even for even in range(0,5,2)],[*list(reversed([odd for odd in range(1,5,2)]))]))))
# n=int(input())
# if n==1:
#     print(1)
#     exit()
# if n==2 or n==3:
#     print('NO SOLUTION')
#     exit()
# a=list(i for i in range(1,n+1) if i%2==0)+list(list(i for i in range(1,n+1) if i%2==1))
# print(*a)
#Pascal traingle -2
# a=1
# e=1
# res=[1]
# for i in range(a):
#     e=e*(a-i)//(i+1)
#     res.append(e)
# print(res)
#Traling Zeros Factorial
# a=int(input())
# i=5
# zero=0
# while a>=i:
#     zero+=a//i
#     i*=5
# print(zero)
#return no of bits of binary power 2^n
# a=int(input())
# M = 1000000007
# print((2**a)%M)
#Codevita minimize sum
# import math
# a=[20,7,5,4]
# i=0
# limit=3
# while i<limit:
#     maxelemindex=a.index(max(a))
#     a[maxelemindex]=math.floor(a[maxelemindex]//2)
#     print(a)
#     i+=1
# print(sum(a))
#find factor of number
# from math import sqrt
# from functools import reduce
# def factors(n):
#         step = 2 if n%2 else 1
#         return set(reduce(list.__add__,
#                     ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))
# x=factors(510510)
# print(x)
# print(len([i for i in x if i==int(sqrt(i))**2]))
#next_permutations
# from itertools import permutations
# list=[''.join(i) for i in permutations(input())]
# print(len(set(list)))
# print(*sorted(set(list)),sep="\n")
#Count Subarray having sum target
# n,target=list(map(int,input().split()))
# arr=list(map(int,input().split()))
# start=arr[0]
# counter=0
# counter+=(start==target)
# pointer=0
# for i in range(1,n):
#     start+=arr[i]
#     while start>target:
#         start-=arr[pointer]
#         pointer+=1
#     counter+=(start==target)
# print(counter)
#even folowed by odd in single list[2,4,6...1,3,5,7.....]
# from collections import deque
# a=deque()
# for i in [3,1,2,4]:
#     if i%2==0:
#         a.appendleft(i)
#     else:
#         a.append(i)
# print(list(a))
# x=[]
# a=[3,1,2,4]
# x=sorted(a,key=lambda  x: x%2)
# print(x)

# a=[5,9,7,9,9]
# if 9 in set(a) and len(set(a))==1:
#     res=[1]+[0]*len(a)
#     print(res)    
# if a[-1]==9:
#     pointer=-1
#     while a[pointer]==9:
#         a[pointer]=0
#         pointer-=1
#     print(a[pointer])
#     a[pointer]=a[pointer]+1
# else:
#     a[-1]=a[-1]+1
# print(a)
# x=0
# #Convert list to int <COOL WAY>
# k=len(a)-1
# for i in a:
#     x+=(10**k)*i
#     k-=1
# print(x)
#even more cool 
# sum(e * 10**i for i, e in enumerate(num[::-1]))
#divide int to digits
# from math import log10
# def digitize(x):
#     sum,multiply=0,1
#     n = int(log10(x))
#     for i in range(n, -1, -1):
#         factor = 10**i
#         k = x // factor
#         sum+=k
#         multiply*=k
#         x -= k * factor
#     return multiply-sum
# print(digitize(234))
#Kids With the Greatest Number of Candies -Leetcode
# a=[12,1,12]
# k=10
# hash={}
# minimum_need=max(a)
# for j,i in enumerate(a):
#     if i+k>=minimum_need and i not in hash:
#         a[j]=True
#         hash[i]=None
#     elif i in hash:
#         a[j]=True

#     else:
#         a[j]=False
# print(a)
#KADENS ALGORITHM FOR MAXIMUM Product array
# def maxProduct(self, nums: List[int]) -> int:
#         # 1. Edge Case : Negative * Negative = Positive
#         # 2. So we need to keep track of minimum values also, as they can yield maximum values.
        
#     global_max = prev_max = prev_min = nums[0]
#     for num in nums[1:]:
#         curr_min = min(prev_max*num, prev_min*num, num)
#         curr_max = max(prev_max*num, prev_min*num, num)
#         global_max= max(global_max, curr_max)
#         prev_max = curr_max
#         prev_min = curr_min
#     return global_max
#Run length encoding Python leetcode
# a=[1,1,2,3]
# res=[]
# for i in range(0,len(a),2):
#     res+=[a[i+1]]*a[i]
# print(res)
# a = [0,1,2,3,4] 
# b = [0,1,2,2,1]
#simple zip leetcode 
# res=[]
# for i,j in zip(a,b):
#     res.insert(j,i)
# print(res)  
# Split a String in Balanced Strings Leetcode  
# s = "RLRRRLLRLL"
# counter=0
# ans=0
# for i in s:
#     if i=='L':
#         counter+=1
#     else:
#         counter-=1
#     if counter==0:
#         ans+=1
# print(ans)

#2sum leetcode
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         checked={}
#         for i,value in enumerate(nums):
#             remaning=target-value
#             if remaning in checked:
#                 return [i,checked[remaning]]
#             else:
#                 checked[value]=i
#2Sum Hackerrank
# a=[1,5,3,4,2]
# k=1
# check={}
# for i,val in enumerate(a):
#     remaning=k-val
#     if remaning in check:
#         print([i+1,check[remaning]+1],'xxxxxx')
#     else:
#         check[val]=i
# def _change_matrix(coin_set, change_amount):
#     matrix = [[0 for m in range(change_amount + 1)] for m in range(len(coin_set) + 1)]
#     for i in range(change_amount + 1):
#         matrix[0][i] = i
#     return matrix

# def change_making(coins, change):
#     matrix = _change_matrix(coins, change)
#     for c in range(1, len(coins) + 1):
#         for r in range(1, change + 1):

#             if coins[c-1] == r:
#                 matrix[c][r] = 1

#             elif coins[c-1]:
#                 matrix[c][r] = matrix[c-1][r]

#             else:
#                 matrix[c][r] = min(matrix[c - 1][r], 1 + matrix[c][r - coins[c - 1]])

#     return matrix[-1][-1]


# print(change_making([2,5,3,6], 10))
#Continously break number till sum of number ==1 HALFSOLUTION
# import math
# n=19
# i=20
# while x!=1 and
#     x=sum([((n//(10**i))%10)**2 for i in range(math.ceil(math.log(n, 10))-1, -1, -1)])
#XOR-Querries on array
# from functools import reduce
# arr=[4,8,2,10]
# queries = [[2,3],[1,3],[0,0],[0,3]]
# res=[]
# from operator import xor
# for i in queries:
#     up,low=i
#     res.append(reduce(xor,arr[up:low+1]))
# print(res)
#template of finding last minimum and last maximum index from array
# def lastminmax(a):
#     mi=mx=0
#     for i in range(len(a)):
#         if a[mi]>=a[i]:
#             mi=i
#         if a[mx]<=a[i]:
#             mx=i
#     return mi,mx
# a=[10,30,5,70,90,5,100,20,700,1,20,700,1]
# mi,mx=lastminmax(a)
# print(mi,mx)
#binary search
# import random
# def binarysearch(arr,target,l,r):
#     while l<=r:
#         mid=l+(r-l)//2
#         if a[mid]==target:
#             return f'{target} found at {mid}'
#         if a[mid]<target:
#             l=mid+1
#         else:
#             r=mid-1
#     return -1
# a=[random.randint(1,100) for i in range(100)]
# l,r=0,len(a)-1
# x=binarysearch(a,target,l,r)
# print(x)
#weirdalgo distincet nummbers
# y=input()
# x=set(input())
# print(len(x))
#weird algo max sum sub array
size=4
arr=[33, 44 ,11 ,22]
mi=mx=0
for i in range(len(arr)):
    if arr[mi]>=arr[i]:
        mi=i
    if arr[mx]<arr[i]:
        mx=i
print(mx,mi)
if mx>mi:
    size-=1
    print((size-mi)+mx-1)
else:
    print((size-mi)+mx-1)
from math import log10
from collections import deque
def digitize(num):
    digits = deque()
    while True:
        num,r = divmod(num,10)
        digits.appendleft(r)
        if num == 0:
            break
    return list(digits)
x=list(map(str,[3,30,34,5,9]))
x.sort(key= lambda x: x[0],reverse=True)
print(x)
def adjacent_find(xs):
    '''Does the supplied iterable contain any adjacent repeats?
    
    Returns True if xs contains two consecutive, equal items,
    False otherwise. 
    '''
    try:
        curr, next_ = tee(xs)
        next(next_)
        return any(c == n for c, n in zip(curr, next_))
    except StopIteration:
        return False
#print(adjacent_find([1,2,3,4,5]))
 #binary search closest smallest and largest of x
def greatesvalueclosetox(array,x):
    l=-1
    r=len(array)
    while r>l+1:
        mid=(l+r)//2
        if array[mid]>=x:
            r=mid
        else:
            l=mid   
    return [l,r]
print(greatesvalueclosetox([1,3,5,6],5))
#find minimum xor pairs whose sum equal to n
n=5
m = n
while m & (m-1):
    m = m & (m-1)
print((n-m),m)
#find comon factors of two numbers for big inputs
res=[]
from math import gcd
from math import sqrt
n1,n2=50,100
def cf(num1,num2):
    n=[]
    g=gcd(num1, num2)
    for i in range(1, int(sqrt(g))+1):
        if g%i==0:
            n.append(i)
            if g!=i*i:
                n.append(int(g/i))
    return n

print(len(cf(n1,n2)))
#convert int to reverse int without converting to string
def reverseint(n):
    #note 100==>1
    x, res = n, 0
    f = lambda: (res * 10) + x % 10
    while x > 0:
        x, res = x//10 , f()
    return [res,n]
print(reverseint(121))