filter= lambda x:x if x % 2 == 0 else None
arr= [1,2,3,4,5,6,7,8,9,10]
ans=[]
for i in arr:
    if filter(i)!=None:
      ans.append(filter(i))
print(ans)

