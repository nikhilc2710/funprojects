# Count number of ones in very long binary represnation
# https://leetcode.com/problems/number-of-1-bits/
# 11111111111111111111111111111101 carzy long numbers
# Logic:
# like int n%10 number is binary so we use n%2 if yes increament ans 
# and instead of n//10 we do n//2 to get rid of last digit
    def hammingWeight(self, n: str) -> int:
        ans=0
        while n:
            if n%2: ans += 1
            n//=2
        return ans

# Add two numbers without any arithemetic operators #IMP# 
        MASK=0xffffffff #to round up reslut and loop upto 32 bit
        while b & MASK:
            carray=a & b
            a=a^b
            b=carray<<1
        return (a & MASK) if b>0 else a