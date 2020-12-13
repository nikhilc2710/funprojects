#Day1
#ps https://leetcode.com/problems/detect-capital/
#isupper()=> check string is Uppercase or not
#islower()=>check string is lowercase or not
#istitie()=> return True only if first letter of string is capital else False 'AhhxxAA'.istitle()=> False Google =>True
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return True if word.isupper() or word.islower() or word.istitle() else False
#Day2
#design set
#ps https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3410/
#set.add(int:value) add item to hash
#set.remove(value) remove value from set
#a in set # return a exist in set or not
#day3
#ps https://leetcode.com/problems/valid-palindrome/
#regex approch let system do the job
#(r'[^\w]|_',"",s) remove all the puncations (, : _) and empty sapces
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=re.sub(r'[^\w]|_',"",s).lower() 
        return True if s==s[::-1] else False
#day 4
#power of 4 16=> true 15=> False
#soln1
#ps:https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3412/
import math
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num>0 and math.log(num,4).is_integer() 
 #soln2
 # idea
 # number is power of four only if there is only one "1" is present
 # 100(4) (10000)(16) and one must be present at odd position to satisfy power of 4   
 def isPowerOfFour(self, num: int) -> bool:
    if num<=0:return False
    if num&num-1 !=0: return False #check if there only 1 is present or not 
    b=bin(num)[::-1] #revese the string to get correct positon
    p=b.index("1")
    return p%2==0   #checking for even because of 0 indexing
#day 6
#ps https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3414/
#just use counter if there are sums like count no of items in array
from collections import Counter
count=Counter(nums)
return [i for i in count if count[i]>1 ]
#soln2
#other soln
#in question its given number of elements are <=size off array
#so we can use this array as lookup like if we saw 4 we make the 4th index negative next time we see that index is negative we know it repated twice
arr=[4,3,2,7,8,2,3,1]
op=[]
for i in arr:
    x=abs(i) #to take care negative value edge case
    if arr[x-1]<0: #it means we seen this element before
        op.append(x)
    else:
        nums[x-1]*=-1 #if we see first time that number we make that index negative
#day7
#ps
#vertical order travesl of binary tree
#traverse tree vertically

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        mapper=defaultdict(list)
        def dfs(x,y,node):
            if not node:
                return
            dfs(x-1,y+1,node.left) #go to left part level by level
            dfs(x+1,y+1,node.right) #go to right side level by leve
            mapper[(x,y)].append(node.val) #add the values to the list
        dfs(0,0,root)
        output=[]
        old=float('-inf') #keep track of x cord (horizontal)
        for k,v in sorted(mapper.items()):
            if k[0]!=old: #if x cord changes #basically for every x new list will be created
                output.append([])
            output[-1].extend(sorted(v)) #we add all the x cord values to that list
            old=k[0]
        return output
