# while True:
#     i=int(input())
#     if i==42:
#         break
#     else:
#         print(i)
#filterinner arrays
from operator import itemgetter
restaurants =  [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]
veganFriendly = 0
maxPrice = 50
maxDistance = 10

r=[]
vegindex=2
priceindex=3
distance=4
for index,i in enumerate(restaurants):
    if veganFriendly==1:
        if i[vegindex]==1 and i[priceindex]<=maxPrice  and i[distance]<=maxDistance:
            r.append([i[1],index+1])
    else:
        if i[priceindex]<=maxPrice and i[distance]<=maxDistance:
            r.append([i[1],index+1])
r.sort(key=itemgetter(0),reverse=True)
r=[i[1] for i in r]
print(r)  
#filter template to find multiple values from nested list            
# filtered = (
# (rating, rest_id) for rest_id, rating, vegan, price, distance in restaurants if (vegan or not veganFriendly) and price <= maxPrice and distance <= maxDistance
# )
# return [rest_id for _, rest_id in sorted(filtered, reverse=True)]
#return good pairs i.e same element at greater index [1,23,1,1]=3(0,2)(0,3)(2,3)
# a=[1,2,3,1,1,3]
# a.sort()
# from itertools import groupby
# def helper(n):
#     return n*(n-1)//2
# v=list(len(list(v)) for k,v in groupby(a))
# print (sum(list(map(helper,v))))
#return sum and multiplication of list without converting to string <COOL WAY>
# from functools import reduce
# from operator import mul
# class Solution:
#     def subtractProductAndSum(self, n: int) -> int:
#         def digitize(n, base=10):
#             if n == 0:
#                 yield 0
#             while n:
#                 n, d = divmod(n, base)
#                 yield d
#         l=list(digitize(n))
#         return reduce(mul,l)-sum(l)