import sys

N=int(sys.stdin.readline())
lst=list(map(int,sys.stdin.readline().split()))
dp=[x for x in lst]
for i in range(N):
    for j in range(i):
        if lst[i]>lst[j]:
            dp[i]=max(lst[j]+dp[i],dp[i])

print(max(dp))