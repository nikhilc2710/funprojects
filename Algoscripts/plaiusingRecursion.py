S="racecar"

def ispali(s):
    if len(s)<1:
        return True
    elif s[0]==s[-1]:
        return ispali(s[1:-1])
    else:
        return False
print(ispali(S))
