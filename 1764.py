import sys


N,M=map(int,sys.stdin.readline().split())
A=[]
B=[]
C=[]
count=0
for i in range(N):
    nohear=sys.stdin.readline()
    A.append(nohear)

for j in range(M):
    nosee=sys.stdin.readline()
    B.append(nosee)


check={num:True for num in A}

for i in B:
    if i in check:
        C.append(i)
        count+=1
C.sort()
print(count)
for i in C:
    print(i,end='')
