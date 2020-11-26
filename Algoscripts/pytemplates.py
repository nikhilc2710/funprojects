import sys
from collections import Counter
from math import gcd
 
def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')
sys.setrecursionlimit(10 ** 9)
INF = 10 ** 19
MOD = 10 ** 19 + 7
EPS = 10 ** -10
 
N = INT()
K = 10**9
L = 10**18
A = [0] * N
C = Counter()
for i in range(N):
    a = float(input())
    A[i] = round(a * K)
    C[gcd(A[i], L)] += 1
 
ans = 0
for k1, v1 in C.items():
    for k2, v2 in C.items():
        if k1 == k2:
            if k1*k2 % L == 0:
                ans += v1*(v1-1) // 2
        elif k1 < k2:
            if k1*k2 % L == 0:
                ans += v1 * v2
print(ans)