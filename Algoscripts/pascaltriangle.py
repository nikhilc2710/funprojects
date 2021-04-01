n=9
dp=[["" for i in range(n)] for _ in range (n)]

for row in range(n):
    for col in range(n):
        if col==0 or col==row:
            dp[row][col]=1
        else:
            dp[row][col]=dp[row-1][col-1]+dp[row-1][col]

print(*dp,sep="\n")
