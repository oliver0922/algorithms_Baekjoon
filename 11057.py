import sys

N=int(sys.stdin.readline())

dp=[[1 for i in range(10)] for j in range(N)]
for i in range(1,N):
    for j in range(1,10):
        dp[i][j]=0
        for k in range(j+1):
            dp[i][j]+=dp[i-1][k]
        dp[i][0]=1
cnt=0
for i in range(10):
    cnt+=dp[N-1][i]


print(cnt%10007)
