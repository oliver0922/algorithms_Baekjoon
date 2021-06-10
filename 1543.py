import sys

A=list(sys.stdin.readline().strip())#문서
B=list(sys.stdin.readline().strip())#검색문자

maximum=0
i=0

while i<=(len(A)-len(B)):
    count=0
    c=0
    for j in range(len(B)):
        if A[i+c]==B[j]:
            count+=1
            c+=1
            continue
        else:
            break
    if count==len(B):
        i+=len(B)
        maximum+=1
    else:
        i+=1
  

print(maximum)


            
