def maxSubarray(i,l,j,max):
   s=0
   for i in range(i,j+1):
        s+=l[i]
   if s>max:
        max=s
   return max
      
def subarray(l,n,max):
    if len(l)==0:
        print("empty array")
    else:
      for i in range(n):
        for j in range(i,n):
            max=maxSubarray(i,l,j,max)
    return max
N=int(input())
arr=list(map(int,input().split()))
max=0
c=subarray(arr,N,max)
print(c)