def countNum(n,count):
    if n==0:
        print(count)
    else:
        count+=1
        countNum(n//10,count)

n=int(input())
count=0
countNum(n,count)