N=int(input())
arr=list(map(int,input().split()))
ind=list(map(int,input().split()))
s=0
for i in range(ind[0],ind[1]+1):
    s+=arr[i-1]
print(s)
      