import sys

t=int(sys.stdin.readline())
for i in range(t):
    n=int(sys.stdin.readline())
    a=[None]*n
    for j in range(n):
        a[j]=sys.stdin.readline().rstrip()
        #a[j]=(a[j],len(a[j]))
    a.sort()
    
   

    flag=0
    for i in range(n-1):
        limit=len(a[i])
        if a[i] == a[i+1][:limit]:
                print('NO')
                flag+=1
                break
    if flag==0:    
        print('YES')
    
                
        

