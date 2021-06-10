import sys

n=int(sys.stdin.readline())

candidate=[0]
for i in range(n):
    a=int(sys.stdin.readline())
    candidate.append(a)


dp=[0 for _ in range(10000+1)]

dp[1]=candidate[1]
if n>=2:
    dp[2]=candidate[1]+candidate[2]
if n>=3:
    dp[3]=max(candidate[1]+candidate[2],candidate[1]+candidate[3],candidate[2]+candidate[3])
for i in range(4,n+1):
    dp[i]=max(dp[i-3]+candidate[i]+candidate[i-1],dp[i-2]+candidate[i],dp[i-1],dp[i-1]-candidate[i-1]+candidate[i])


print(dp[n])
