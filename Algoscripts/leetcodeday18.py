#GoatLatin
# from collections import Counter
# vowels=Counter('aeiouAEIOU')
# string="zzGPuClvxA XYbNe".split()
# for index,words in enumerate(string):
#     if words[0] in vowels:
#         string[index]=words+'ma'+'a'*index
#     else:
#         temp=words[0]
#         words=words[1::]+temp+'ma'+'a'*(index+1)
#         string[index]=words
# print(*string)
#LongestCommonprefix
# from itertools import groupby
# x=["flower","flow","flight"]
# x.sort()
# res=''
# for i in x[0]:
#     if x[-1].startswith(res+i):
#         res+=i
#     else:
#         break
# print(res)
#Find Right Interval [3,4],[2,3][1,2]=>[-1,0,1] #BINARY SEARCH

# a=[[3,4],[2,3],[1,2]]
# # if not a:
# #     return []
# N=len(a)
# # if N==1:
# #     return[-1]
# result=[-1]*N
# intervals_with_index=[[j,k,i] for i,[j,k] in enumerate(a)] #Append index of interval to the intervals [[0index, 3, 4], [1, 1, 2], [2, 2, 3]]
# intervals_with_index.sort()#sort index based on elements
# for [_,end,index] in intervals_with_index:
#     #start of binary search
#     lo=0
#     hi=len(a)
#     while lo!=hi:
#         mid=lo+(hi-lo)//2
#         if intervals_with_index[mid][0]<end:
#             lo=mid+1
#         elif intervals_with_index[mid][0]>=end:
#             hi=mid
#     if lo!=N:
#         _,_,target_index=intervals_with_index[lo]
#         result[index]=target_index

# print(result)
a='ababcbacadefegdehijhklij'
lastindex={i:[a.find(i),a.rfind(i)] for i in a}
start,end=list(zip(*lastindex.values()))
print(start)
print(end)
# res=set()
# temp=0
# lookup=set()
# for i in a:
#     if i not  in lookup:
#         charstart,charend=lastindex[i]
#         for j in lastindex:
#             if lastindex[j][0]<charend:
#                 temp=max(charend,lastindex[j][1])
#                 lookup.add(j)
#             res.add(temp)
# print(res)
# print(len(res))



