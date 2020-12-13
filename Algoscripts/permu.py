import secrets
from collections import defaultdict

x=0
randomlist = []
while x<100:
    y=secrets.choice(range(1,11))
    randomlist.append(y)
    x=x+1

ddict = defaultdict(list)
for i,r in enumerate(randomlist):
    ddict[r].append(i)
print(len(ddict))
x=0
for k,v in ddict.items():
    # if len(v)>=2:
    #     print("even sum - " + str(k) + " : " + str(v))
    for i,j in ddict.items():
        if (k+i)%2==0 and k!=i:
            x+=1
            print(x)
            # print("even sum - " + str(k) + " : " + str (i)+ " : " + str(v) + str(j))