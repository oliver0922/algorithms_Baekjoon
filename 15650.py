import sys

N,M=map(int,sys.stdin.readline().split())

def backtracking(ans,num):

    if len(ans)==M:
        for i in ans:
            print(i,'',end='')
        print()
        return

    candidate=list(range(1,N+1))

    for i in range(len(ans)):
        if ans[i] in candidate:
            candidate.remove(ans[i])

    for i in candidate:
        if len(ans)==0:
            ans.append(i)
            backtracking(ans,num)
            ans.pop()
        else:
            if i>max(ans):
                ans.append(i)
                backtracking(ans,num)
                ans.pop()
            else:
                continue
                    

backtracking([],M)
    
