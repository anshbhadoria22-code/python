def totalSubarray(i,l,j):
   s=0
   totalsum=0
   for i in range(i,j+1):
        s+=l[i]
   return s

def subarray(l,n):
    if len(l)==0:
        print("empty array")
    else:
      total_sum=0
      for i in range(n):
        for j in range(i,n):
            total_sum+=totalSubarray(i,l,j)
      print(total_sum)
N=int(input())
arr=list(map(int,input().split()))
subarray(arr,N)