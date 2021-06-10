import sys

N,M=map(int,sys.stdin.readline().split())
A=list(map(int,sys.stdin.readline().split()))
B=list(map(int,sys.stdin.readline().split()))

C={num:True for num in A}
count=0
for i in B:
    if i in C:
       count+=1

print(len(A)+len(B)-2*count)
