#Longest Common perfix
#flower flow flee => 2
#Idea:
#sort() list
#check first and last word how much they match
######CODE#########
class Solution:
    def solve(self, words):
        words.sort()
        res=''
        for i in words[0]:
            if words[-1].startswith(res+i):
                res+=i
            else:
                break
        return res