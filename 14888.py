import sys
from collections import deque

N=int(sys.stdin.readline())
operand=list(map(int,sys.stdin.readline().split()))#피연산자
operator=list(map(int,sys.stdin.readline().split()))#연산자
op=[]
operand=deque(operand)
for i in range(len(operator)):
    for j in range(operator[i]):
        if i==0:
            op.append('+')
        elif i==1:
            op.append('-')
        elif i==2:
            op.append('*')
        else:
            op.append('/')


real=[]
def backtracking(sol,op,operand):


    if len(sol)==len(op):
        answer=[operand[0]]
        i=0
        j=1
        while i!=len(op):
            x=answer.pop()
            y=operand[j]
            z=sol[i]
            if z=='+':
                ans=x+y
                answer.append(ans)
            elif z=='-':
                ans=x-y
                answer.append(ans)
            elif z=='*':
                ans=x*y
                answer.append(ans)
            else:
                if x<0:
                    ans=-((-x)//y)
                else:
                    ans=x//y
                answer.append(ans)
            i+=1
            j+=1
        global real
        real.append(answer[0])
        return 
    candidate=[]
    for i in op:
        candidate.append(i)
        
    for i in range(len(sol)):
        if sol[i] in candidate:
            candidate.remove(sol[i])

    for i in candidate:
        sol.append(i)
        backtracking(sol,op,operand)
        sol.pop()

    


        
backtracking([],op,operand)

print(max(real))
print(min(real))
    

    
        
