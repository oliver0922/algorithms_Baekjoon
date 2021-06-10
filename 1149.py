import sys
N=int(sys.stdin.readline())
street=[]


for i in range(N):
    home=list(map(int,sys.stdin.readline().split()))
    street.append(home)
dp=[[] for i in range(N)]

dp[0].append(street[0][0])
dp[0].append(street[0][1])
dp[0].append(street[0][2])

for i in range(1,N):
    dp[i].append(min(dp[i-1][1]+street[i][0],dp[i-1][2]+street[i][0]))
    dp[i].append(min(dp[i-1][0]+street[i][1],dp[i-1][2]+street[i][1]))
    dp[i].append(min(dp[i-1][0]+street[i][2],dp[i-1][1]+street[i][2]))

print(min(dp[N-1][0],dp[N-1][1],dp[N-1][2]))










