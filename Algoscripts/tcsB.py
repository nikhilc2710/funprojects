a=int(input())
b=list(map(int,input().split()))
c=max(b)
representation=len(f'{c:b}')
# print(f'{2:0{representation}b}')
def binary_formatter(b):
    return f'{b:0{representation}b}'
binaryarray=[[i.count('0'),i.count('1')] for i in list(map(binary_formatter,b))]
print(*binaryarray,sep="\n")
if a==1:
    if len(set(*binaryarray))==1:
        print(f'{1:0{representation}b}')
    else:
        print(f'{0:0{representation}b}')
    exit()

lookup={tuple(sorted(i)) for i in binaryarray}
zeros,ones=0,0
equivalancepair=len(binaryarray)-len(lookup)
for i in range(len(binaryarray)):
    zeros+=binaryarray[i][0]
    ones+=binaryarray[i][1]
    if len(set(binaryarray[i]))==1:      
        equivalancepair+=1
equivalancepair+=(zeros==ones)
print(f'{equivalancepair:0{representation}b}')


