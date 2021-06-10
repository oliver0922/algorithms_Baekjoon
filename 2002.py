import sys

N=int(sys.stdin.readline())
income={}
outcome={}
for i in range(N):
    income_=sys.stdin.readline().strip()
    income[i]=income_ #income={1:A,2:B,3:C}

for i in range(N):
    outcome_=sys.stdin.readline().strip()
    outcome[i]=outcome_#outcome={1:B,2:C,3:A}


count=0

for i in range(N):
    income_value=income[i]#C    
    for j in range(i):
        income_value2=income[j]#비교대상A,B
        list_of_values=list(outcome.values())#[B,C,A]
        a=list_of_values.index(income_value2)#1
        b=list_of_values.index(income_value)#2
        if b<a:
            count+=1
            break
        
        

print(count)
