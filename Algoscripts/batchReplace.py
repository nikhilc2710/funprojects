vowels={'a':'%','e':'%','i':'%','o':'%','u':'%'}
constants={chr(i).lower():'#' for i in range(65,91) if chr(i).lower() not in vowels}
s=input().split()
ans=[0]*len(s)
for i in range(0,len(s),3):
    ans[i]=s[i].translate(str.maketrans(vowels))

for i in range(1,len(s),3):
    ans[i]=s[i].translate(str.maketrans(constants))
for i in range(2,len(s),3):
    ans[i]=s[i].upper()
print(' '.join(ans))
