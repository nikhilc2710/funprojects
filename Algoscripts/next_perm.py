from itertools import permutations
list=[''.join(i) for i in permutations('aaabc')]
print(len(set(list)))
print(*set(list),sep="\n")