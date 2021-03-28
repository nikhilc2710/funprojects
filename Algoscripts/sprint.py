# import random
# from itertools import chain
# a=[55,33,65,23,66,78,70,230,10,11,56,78]
# a.sort(key=lambda  x: [x%2,x])

# def digitize(n):
#     ans=0
#     while n>0:
#         ans+=n%10
#         n=n//10
#     return ans
# # print(digitize(55))

# b=a[::-1]
# s=""
# for i,j in enumerate(zip(a,b)):
#     if not i%3 and i>0:
#         s+=' '
#     s+=''.join(map(str,j))
# # print(s)
# a=[35, -42, 23 ,-56, -84, 92, 39]
# # a=[-11 ,-2 ,19 ,37 ,64 ,-18]
# temp=[]
# k=4

# ans=[]
# # for i in range(len(a)-k+1):
# #     temp.append(a[i:i+k])

# # for i in temp:
# #     Flag=True
# #     for j in i:
# #         if j<0:
# #             Flag=False
# #             i.append(Flag)
# #             break

# # for i in temp:
# #     if not i[-1]:
# #         for j in i:
# #             if j<0:
# #                 ans.append(j)
# #                 break
# #     else:
# #         ans.append(0)
        
# # print(ans)
# ########More clear ans straigtforward soln
# for i in range(len(a)-k+1):
#     for x in a[i:i+k]:
#         if x<0:
#             ans.append(x)
#             break
#     else:
#         ans.append(0)
# print(ans)

def ways(x, coins):
    def helper(n):
        if n==0:
            return 1
        if n<0:return 0
        inc=exc=0
        for i in coins:
            inc=helper(n-i)
            exc=helper(n)
        return inc+exc
    return helper(x)
# print(ways(4,set([1,2,3])))

from math import sqrt,gcd
def cf(n1,n2):
    n=[]
    g=gcd(n1,n2)
    for i in range(1,int(sqrt(g))+1):
        if g%i==0:
            n.append(i)
            if g!=i*i:
                n.append(g//i)
    return(n)
print(cf(100,150))
from math import sqrt
from itertools import count, islice

def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))
print(is_prime(8))
