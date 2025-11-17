def sumNum(n,sum):
    if n==0:
        return sum
    else:
        d=n%10
        sum=sum+d
        return sumNum(n//10,sum)

n=int(input())
sum=0
sum=(sumNum(n,sum))
print(sum)