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

############Even more optimized #####################
from itertools import chain
vowels={'a':'%','e':'%','i':'%','o':'%','u':'%'}
constants={chr(i).lower():'#' for i in range(65,91) if chr(i).lower() not in vowels}
s=input().split()
z=' '.join((chain(*zip(*[[i.translate(str.maketrans(vowels)) for i in s[0:len(s):3]],[i.translate(str.maketrans(constants)) for i in  s[1:len(s):3]],[i.upper() for i in s[2:len(s):3]]]))))
print(z)
