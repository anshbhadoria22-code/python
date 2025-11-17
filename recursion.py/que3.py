def printN(n,i):
    if i==n:
        print(i)
        return
    else:
        print(i)
        printN(n,i+1)
    
n=int(input())
i=1
printN(n,i)