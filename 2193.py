import sys

N=int(sys.stdin.readline())

dp=[0 for i in range(91)]

dp[1]=1
dp[2]=1

for j in range(3,N+1):
    dp[j]=dp[j-2]+dp[j-1]


print(dp[N])
