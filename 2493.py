import sys


n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))



stack=[]
receiver=[]


for i in range(n):
    while stack:
        if stack[-1][1]>a[i]:
            receiver.append(stack[-1][0]+1)
            break
        else:
            stack.pop()

    if not stack:
        receiver.append(0)
    stack.append([i,a[i]])
        

for i in range(n):
    print(receiver[i],'',end='')
            
            
    
    
