import sys

N=int(sys.stdin.readline())
lst=list(map(int,sys.stdin.readline().split()))
dp=[1 for i in range(N)]
candidate=[]
for i in range(N):
    a=[]
    for j in range(i):
        if lst[i]>lst[j]:
            if dp[i]<dp[j]+1:
                dp[i]=dp[j]+1
                a.append(lst[j])
                if dp[j]==dp[j+1]:
                    a.pop()
                    a.append(lst[j+1])
    a.append(lst[i])
    candidate.append(a)

print(max(dp))
b=candidate[dp.index(max(dp))]
#print(candidate)
for i in b:
    print(i,'',end='')
print()