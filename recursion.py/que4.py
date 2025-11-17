def printN(n):
    if n==0:
        return
    else:
        print(n)
        printN(n-1)
n=int(input())
printN(n)