def pow(n,x,p):
    if x==0:
        return p
    else:
        p*=n
        return pow(n,x-1,p)
n=int(input())
x=int(input())
p=1
power=pow(n,x,p)
print(power)