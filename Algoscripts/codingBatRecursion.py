from typing import List



def groupSumClump (start : int , arr : List [int] , target : int) -> None:
    def groupby (toCompress : List [int]) -> List[int]:
        N : int = len (toCompress)
        i : int = 0
        compressedSum : int =  0
        while i <N:
            temp : int = toCompress [i]
            j : int = i + 1
            while j < N:
                if toCompress [i] == toCompress[j]:
                    j +=1
                    compressedSum += toCompress [j]
                else :
                    break
            toCompress [i] += compressedSum
            i = j+1
        return toCompress
            
                
                
    N : int = len(arr)-1
    arr = [2, 4, 4, 8]
    arr = groupby (arr)
    print (arr)
groupSumClump(0, [2, 4, 8], 10) → true	false	X	
groupSumClump(0, [1, 2, 4, 8, 1], 14) → true	false	X	
groupSumClump(0, [2, 4, 4, 8], 14) → false	false	OK	
groupSumClump(0, [8, 2, 2, 1], 9) → true	false	X	
groupSumClump(0, [8, 2, 2, 1], 11) → false	false	OK	
groupSumClump(0, [1], 1) → true	false	X	
groupSumClump(0, [9], 1) → false

def groupSum5 (start : int , arr : List [int] , target : int) -> None:
    N : int = len(arr)-1
    def solve (i : int , sumSoFar : int) -> bool:
        if sumSoFar == target:
            return True
        if sumSoFar > target or i > N:
            return False
        
        return solve (i+2,sumSoFar + arr[i]) or solve (i+1,sumSoFar) 
    for i in arr:
        if not i%5:
            sumSoFar += i
    ans = solve (start , sumSoFar)
    print (ans)


groupSum5(0, [2, 5, 10, 4], 19) → true	false	X	
groupSum5(0, [2, 5, 10, 4], 17) → true	false	X	
groupSum5(0, [2, 5, 10, 4], 12) → false	false	OK	
groupSum5(0, [2, 5, 4, 10], 12) → false	false	OK	
groupSum5(0, [3, 5, 1], 4) → false	false	OK	
groupSum5(0, [3, 5, 1], 5) → true	false	X	
groupSum5(0, [1, 3, 5], 5) → true	false	X	
groupSum5(0, [3, 5, 1], 9) → false	false	OK	
groupSum5(0, [2, 5, 10, 4], 7) → false	false	OK	
groupSum5(0, [2, 5, 10, 4], 15) → true	false	X	
groupSum5(0, [2, 5, 10, 4], 11) → false	false	OK	
groupSum5(0, [1], 1) → true	false	X	
groupSum5(0, [9], 1) → false	false	OK	
groupSum5(0, [9], 0) → true	false	X	
groupSum5(0, [], 0) → true



def groupNoAdj (start : int , arr : List [int] , target : int) -> None:
    N= len(arr)-1
    def solve (i : int , sumSoFar : int) -> bool:
        if sumSoFar == target:
            return True
        if sumSoFar > target or i > N:
            return False
        
        return solve (i+2,sumSoFar + arr[i]) or solve (i+1,sumSoFar) 
    ans = solve (start , 0)
    print (ans)

groupNoAdj(0, [2, 5, 10, 4], 12) #→ true	false	X	
groupNoAdj(0, [2, 5, 10, 4], 14) #→ false	false	OK	
groupNoAdj(0, [2, 5, 10, 4], 7) #→ false	false	OK	
groupNoAdj(0, [2, 5, 10, 4, 2], 7)# → true	false	X	
groupNoAdj(0, [2, 5, 10, 4], 9) #→ true	false	X	
groupNoAdj(0, [10, 2, 2, 3, 3], 15)# → true	false	X	
groupNoAdj(0, [10, 2, 2, 3, 3], 7) #→ false	false	OK	
groupNoAdj(0, [], 0) #→ true	false	X	
groupNoAdj(0, [1], 1) #→ true	false	X	
groupNoAdj(0, [9], 1) #→ false	false	OK	
groupNoAdj(0, [9], 0) #→ true	false	X	
groupNoAdj(0, [5, 10, 4, 1], 11) #→ true	false





def groupSum6 (start : int , arr : List[int],target : int) -> bool:
    N = len (arr) -1
    def solve (i : int , sumSoFar):
        if sumSoFar == target:
            return True
        if sumSoFar > target or i > N:
            return False
        return solve (i+1,sumSoFar + arr[i]) or solve (i+1,sumSoFar)
    sumSoFar = 0
    for i in arr:
        if i ==6:
            sumSoFar += i
    ans = solve (start,sumSoFar)
    print (ans)
    
groupSum6(0, [5, 6, 2], 8) #→ true	false	X	
groupSum6(0, [5, 6, 2], 9) #→ false	false	OK	
groupSum6(0, [5, 6, 2], 7) #→ false	false	OK	
groupSum6(0, [1], 1) #→ true	false	X	
groupSum6(0, [9], 1) #→ false	false	OK	
groupSum6(0, [], 0) #→ true	false	X	
groupSum6(0, [3, 2, 4, 6], 8) #→ true	false	X	
groupSum6(0, [6, 2, 4, 3], 8) #→ true	false	X	
groupSum6(0, [5, 2, 4, 6], 9) #→ false	false	OK	
groupSum6(0, [6, 2, 4, 5], 9) #→ false	false	OK	
groupSum6(0, [3, 2, 4, 6], 3) #→ false	false	OK	
groupSum6(0, [1, 6, 2, 6, 4], 12) #→ true	false	X	
groupSum6(0, [1, 6, 2, 6, 4], 13) #→ true	false	X	
groupSum6(0, [1, 6, 2, 6, 4], 4) #→ false	false	OK	
groupSum6(0, [1, 6, 2, 6, 4], 9) #→ false	false	OK	
groupSum6(0, [1, 6, 2, 6, 5], 14) #→ true	false	X	
groupSum6(0, [1, 6, 2, 6, 5], 15) #→ true	false	X	
groupSum6(0, [1, 6, 2, 6, 5], 16) #→ false



























def groupSum (start ,arr : List [int], target : int ) -> bool:
    N = len(arr)-1
    def solve (i : int ,sumSoFar : int, sumList,ind : str = ""):
        if sumSoFar == target:
            print (sumList,target)
            return True
        if  i > N or sumSoFar > target:
            return False
        return solve (i+1, sumSoFar + arr[i],sumList + [arr[i]],"include") or \
        solve (i+1,sumSoFar,sumList,"not inc")
    ans = solve (start,0,[])
    print (ans)
        
	
groupSum(0, [2, 4, 8], 10) #→ true	true	OK	
groupSum(0, [2, 4, 8], 14) #→ true	true	OK	
groupSum(0, [2, 4, 8], 9) #→ false	true	X	
groupSum(0, [2, 4, 8], 8) #→ true	true	OK	
groupSum(1, [2, 4, 8], 8) #→ true	true	OK	
groupSum(1, [2, 4, 8], 2) #→ false	true	X	
groupSum(0, [1], 1) #→ true	true	OK	
groupSum(0, [9], 1) #→ false	true	X	
groupSum(1, [9], 0) #→ true	true	OK	
groupSum(0, [], 0) #→ true	true	OK	
groupSum(0, [10, 2, 2, 5], 17) #→ true	true	OK	
groupSum(0, [10, 2, 2, 5], 15) #→ true	true	OK	
groupSum(0, [10, 2, 2, 5], 9) #→ true

a \
= '''
a
b
c
d
e
f
'''
print (a.strip().split())
a = 52816152 
b = 52816561
print (b-a)
def allStar(s : str) -> str:
    if not s:return ""
    
    L,R = 0,len(s)-2
    def solve (l,ans):
        if l>R:
            return ans + s[-1]
        ans += s[l]+'*'
        return solve(l+1,ans)
    ans = solve(L,"")
    print (ans)
    

allStar("hello")# → "h*e*l*l*o"	""	X	
allStar("abc") #→ "a*b*c"	""	X	
allStar("ab") #→ "a*b"	""	X	
allStar("a") #→ "a"	""	X	
allStar("") #→ #""	""	OK	
allStar("3.14") #→ "3*.*1*4"	""	X	
allStar("Chocolate") #→ "C*h*o*c*o*l*a*t*e"	""	X	
allStar("1234") #→ "1*2*3*4"
def stringClean (s : str) -> None:
    if not s:print ("")
    ans = s[0]

    def solve (index : int ) -> None:
        nonlocal ans
        if index >= len(s):
            print (ans)
            return
        if s[index] == ans[-1]:
            return solve (index+1)
        else:
            ans += s[index]
            return solve (index+1)
    ans = solve (1)
stringClean("yyzzza")# → "yza"	""	X	
stringClean("abbbcdd")# → "abcd"	""	X	
stringClean("Hello") #→ "Helo"	""	X	
stringClean("XXabcYY")# → "XabcY"	""	X	
stringClean("112ab445")# → "12ab45"	""	X	
stringClean("Hello Bookkeeper")# → "Helo Bokeper"
def countPairs( s : str) -> None:
    def solve (str_ : str  ):

            
        if len(str_) <=2:
            return 0
            
        if str_[0] == str_[2]:
            
            return 1+solve (str_[1:])
        else:
            
            return solve (str_[1:])
    ans = solve (s)
    print (ans)
countPairs("axa") #→ 1	1	OK	
countPairs("axax") #→ 2	1	X	
countPairs("axbx") #→ 1	1	OK	
countPairs("hi") #→ 0	1	X	
countPairs("hihih") #→ 3	1	X	
countPairs("ihihhh") #→ 3	1	X	
countPairs("ihjxhh") #→ 0	1	X	
countPairs("") #→ 0	1	X	
countPairs("a") #→ 0	1	X	
countPairs("aa") #→ 0	1	X	
countPairs("aaa") #→ 1	1

