import sys

N=int(sys.stdin.readline())

dp=[[1] for _ in range(10)]
dp[0][0]=0

for i in range(N):
    for j in range(1,9):
        dp[i][j]=dp[i-1][j-1]+dp[i-1][j+1]
    dp[i][0]=dp[i-1][1]
    dp[i][9]=dp[i-1][8]

print(len(dp[N])
      
