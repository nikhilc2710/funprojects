a=[2,4,6,10]
lookup={i:[] for i in a}
target=16
res=[]
# for i in range(len(a)-1):
#     temp=a[i]+a[i+1]
#     remaning=target-temp
#     if remaning in lookup:x
#         res.append([a[i],a[i+1],remaning])
# print(res)
# i=0
# while i<len(a)-1:
#     temp=a[i]+a[i+1]
#     remaning=target-temp
#     if remaning in lookup:
#         res.append([a[i],a[i+1],remaning])
#         i+=2
#     else:
#         i+=1
# print(res)
import sys
arr=set()
keys=0
lookup={}
while True:
    a=sys.stdin.readline().strip()
    if a=='q':
        break
    else:
        if a.isalnum():
            arr.add(a)
        keys+=1

# sys.stdout.write('BLANK KEYS:{}\n'.format(keys-len(arr)))
# sys.stdout.write('TOTAL KEYS:{}\n'.format(keys))
# sys.stdout.write('NUMBER OF  LOCKS:{}\n'.format(len(arr)))
# places={
#     'Malaysia':0
#     'Australia':0
#     'Germany':0
#     'Dubai':0
#     'France'
# }