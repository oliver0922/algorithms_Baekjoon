import sys
from collections import deque

A=sys.stdin.readline().rstrip()
B=sys.stdin.readline().rstrip()
stack=[]
A=deque(A)



for i in A:
    if i!=B[-1]:
        stack.append(i)
    else:
        flag=1
        for k in range(len(B)-1):
            if len(stack)!=0 and stack[len(stack)-1-k]==B[len(B)-2-k]:
                flag=1
            else:
                flag=0
                stack.append(i)
                break
        if flag==1:
            for _ in range(len(B)-1):
                stack.pop()

if len(stack)!=0:
    for i in stack:
        print(i,end='')
else:
    print('FRULA')

            
