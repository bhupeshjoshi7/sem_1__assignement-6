def pascal(n):
    pascc=[1]
    #pasc-current pascal
    for i in range(n-2):
        pascp=pascal(n-1)
        pascc.append(pascp[i]+pascp[i+1])
        #pascp-previous pascal
    if n!=1:
        pascc.append(1)
    return pascc

n=int(input())
for i in range(1,n+1):
    pasc=pascal(i)
    flag=0
    while True:
        if flag==0:
            print(' '*(n-i),end="")
        print(pasc[flag],end=' ')
        flag+=1
        if flag==len(pasc):
            break
    print("")
    
