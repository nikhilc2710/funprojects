#2356 => 3256
from math import log10
def swap(n):
    temp=0
    while n>0:
        k=n%10
        temp=(temp*10)+k
        n//=10
    return temp
def combine(curr,sofar):
    k=int (log10(sofar))+1 if sofar>0 else 0
    return curr*(10**k)+sofar
def twoDigits(n):
    ans=0
    while n>0:
        k=n%100
        x=swap(k)
        ans= combine(x,ans)
        n//=100
    return ans

n=56652532
print(n)
print(twoDigits(n))
