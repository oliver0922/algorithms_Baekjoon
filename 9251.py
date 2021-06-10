import sys
from collections import deque

A=list(sys.stdin.readline().rstrip())
B=list(sys.stdin.readline().rstrip())
A=deque(A)
B=deque(B)

A.appendleft(0)
B.appendleft(0)

matrix=[[0]*len(A) for i in range(len(B))]
lcs=[]
for i in range(1,len(B)):
    for j in range(len(A)):
        if A[j]==B[i]:
            matrix[i][j]=matrix[i-1][j-1]+1
        else:
            matrix[i][j]=max(matrix[i-1][j],matrix[i][j-1])

a=len(A)-1
b=len(B)-1
result=matrix[b][a]
while result!=1:
    if result==matrix[b-1][a]:
        result=matrix[b-1][a]
    elif matrix[b][a-1]==result:
        result=matrix[b][a-1]
    else:
        lcs.append(A[a])
        result=matrix[b-1][a-1]


lcs.reverse()        
                
print(matrix[-1][-1])
print(lcs)
