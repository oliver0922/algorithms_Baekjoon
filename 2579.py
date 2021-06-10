import sys

N=int(sys.stdin.readline())

step=[0 for i in range(301)]
dp=[0 for i in range(301)]

for i in range(1,N+1):
    step[i]=int(sys.stdin.readline())

dp[1]=step[1]
dp[2]=step[1]+step[2]
dp[3]=dp[2]+step[3]

for i in range(4,N+1):
    dp[i]=max(dp[i-2]+step[i],dp[i-3]+step[i-1]+step[i])

print(dp[N])
