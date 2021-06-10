n=int(input(''))
count=1
stack=[]
operation=[]
message='True'
for i in range(n):
    x=int(input(''))


    while count<=x:
        stack.append(count)
        operation.append('+')
        count+=1

    if stack[-1]==x:
        stack.pop()
        operation.append('-')

    else:
        message='False'
        

if message=='False':
    print('NO')

else:
    for i in operation:
        print(i)
        
