#combination sum 1
a=[2,5,3,6]
n=10
target=7
dp=[[] for _ in range(target+1)]
for c in a:
    for i in range(1,target+1):
        if i<c:continue
        if i==c:
            dp[i].append([c])
        else:
            for blist in dp[i-c]:
                dp[i].append(blist+[c])
print(dp[target])
#combination sum2
candidates = [10,1,2,7,6,1,5] 
target = 8
candidates.sort()
dp=[set() for _ in range(target+1)]
dp[0].add(())
for c in candidates:
    for i in reversed(range(len(dp))):
        if dp[i]:
            new_combo = set([combo + (c, ) for combo in dp[i]])
            if i + c <= target:
                dp[i + c] = dp[i + c].union(new_combo)
print(list(map(list, dp[target])))