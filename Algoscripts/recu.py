#fib
def fibn(n):
    if n<2:
        return n
    return fibn(n-1)+fibn(n-2)
# print(fibn(9))

def factorail(n):
    if n<1:
        return 1
    return n*factorail(n-1)
# print(factorail(5))

def powerN(n,exp):
    if exp==0:
        return 1
    else:
        return n*powerN(n,exp-1)
# print(powerN(5,0))


def sumofNums(n):
    if n>0:
        k=n%10
        n=n//10
        return k+sumofNums(n)
    else:
        return n

# print(sumofNums(103))
s="i am crazy for you"
def reversestr(n):
    if n==0:
        return s[0]
    else:
        return s[n]+reversestr(n-1)
# print(reversestr(len(s)-1))

def palirec(s):
    if len(s)<=1:
        return True
    else:
        if s[0]==s[-1]:
            return palirec(s[1:-1])
        else:
            return False
# print(palirec("carrace"))

# s1="ppl"
# s2="apple"
# while s1 and s2:
#     if s1[0]==s2[0]:
#         s1=s1[1:]
#         s2=s2[1:]
#     else:
#         s2=s2[1:]


# print(not s1)

def rec(s1,s2):
    if not s1:
        return True
    if s1 and s2:
        if s1[0]==s2[0]:
            return rec(s1[1:],s2[1:])
        else:
            return rec(s1,s2[1:])
    return False
#print(rec("apple",'apple'))
vows={'a','e','i','o','u'}
def countVows(s,i):
    ans=0
    if i<len(s):
        if s[i] in vows:
            return 1+countVows(s,i+1)
        else:
            return countVows(s,i+1)
    else:
        return 0
    
x=countVows('xdcfvgh',0)
# print(x)

def sumupton(n):
    if n==1:
        return 1
    else:
        return n+sumupton(n-1)
# print(sumupton(10))



s="HELLOOO"
ans=""
prev=""
for j in s:
    if j==prev:
        continue
    else:
        ans+=j
        prev=j
# print(ans)
# TODO: Implement using REcursion

 
arr=[1,2,1,4,5,1]

