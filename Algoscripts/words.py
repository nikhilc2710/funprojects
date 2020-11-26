a=">><<><"
counter=0
for i in range(len(a)//2):
  if a[i]!='>':
    counter+=1
  if a[i+len(a)//2]!='<':
    counter+=1
print(counter)


