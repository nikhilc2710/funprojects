# S="abc"
# def ispali(s,point):
#     if point==-1:
#         return s
#     else:
#         s+=S[point]
#         return ispali(s,point-1)
# z=ispali('',len(S)-1)
# print(z)
x=1
def factorial(n):
    print(n)
    if n<1:
        return 1
    x=x*factorial(n-1)
n=5
print(factorial(n))