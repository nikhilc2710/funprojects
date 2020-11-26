def fibs(n):    
    res=[] #to store result
    for i in range(n):
        if i<2:
            res.append(i) #to append 0,1,2
        else:
            res.append(res[i-2]+res[i-1]) # rest of list
    return res#return result
a=fibs(100)
print(len(a))
###############################
#problem 2 longest palindrome
a="babad"
def longest_plaindrome(string,first,last):
    if first>last:
        return 0
    if first==last:
        return 1
    if string[first]==string[last]:
        return longest_plaindrome(string,first+1,last-1)+2
    if first!=last:
        return max(longest_plaindrome(string,first,last-1),longest_plaindrome(string,first+1,last))
first=0
last=len(a)
x=longest_plaindrome(a,first,last-1)
print(x)

#maximum sub sum sub aray
import sys
a=[-2,1,-3,4,-1,2,1,-5,4]
x=sum(a)
print(x)
result=-sys.maxsize
var=0
for i in a:
    var+=i
    result=max(result,var)
    var=max(var,0)

print(result)
a=[1,4,3,2]
a.sort()
sum(a[::2])
