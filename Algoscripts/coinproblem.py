# import itertools
# a=[]
# arr=[5 ,37 ,8 ,39 ,33 ,17 ,22 ,32 ,13, 7 ,10 ,35, 40 ,2 ,43, 49 ,46, 19 ,41 ,1 ,12 ,11 ,28]
# for i in arr:
#     a.extend([values for values in itertools.product(arr,repeat= i) if sum(values)^166 ==0])
# print(len(a))
import random
import time

a=tuple((random.randint(1,5),random.randint(1,5))  for i in range(20000))
s=time.time()
b=tuple(reversed(i) for i in a)
e=time.time()
print(f'{(e-s)*1000:.2f}')
s=time.time()
b=tuple(sorted(i) for i in a)
e=time.time()
print(f'{(e-s)*1000 :.2f}')