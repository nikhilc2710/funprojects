from itertools import groupby
str=input()
a=int(input())
chiperarr=[]
chainmap={}
for i in range(a):
    chiperarr.append(input().split())
chipermap={}
for i in chiperarr:
    subset_a={i[0].count(j):j for j in i[0]}
    subset_b={i[1].count(j):j for j in i[1]}
    for x in subset_b:
        if subset_b[x] in chainmap or subset_b[x] in chainmap.values():
            chainmap[subset_b[x] ]=subset_a[x]
        else:
            chainmap[subset_b[x] ]=subset_a[x]
            chainmap[subset_a[x] ]=subset_b[x]
            
output=""
print(sorted(chainmap.items()))

for i in str:
    output+=chainmap[i]
print(output)

