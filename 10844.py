import sys

N=int(sys.stdin.readline())

dp=[[ 1 for _ in range(10)] for i in range(N)]
dp[0][0]=0

for i in range(1,N):
    for j in range(1,9):
        dp[i][j]=dp[i-1][j-1]+dp[i-1][j+1]
    dp[i][0]=dp[i-1][1]
    dp[i][9]=dp[i-1][8]

cnt=0
for i in range(10):
    cnt+=dp[N-1][i]

print(cnt%1000000000)
    
      
