def sumSubarray(si,l,ei):
   s=0
   for i in range(si,ei+1):
      s+=l[i]
   print(s)
def subarray(l,n):
    if len(l)==0:
        print("empty array")
    else:
      for i in range(n):
        for j in range(i,n):
            sumSubarray(i,l,j)
N=int(input())
arr=list(map(int,input().split()))
subarray(arr,N)
