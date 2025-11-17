def printSubarray(si,l,ei):
    for i in range(si,ei+1):
        print(l[i],end=" ")
    print()
def subarray(l,n):
    if len(l)==0:
        print("empty array")
    else:
      for i in range(n):
        for j in range(i,n):
            printSubarray(i,l,j)
N=int(input())
arr=list(map(int,input().split()))
subarray(arr,N)