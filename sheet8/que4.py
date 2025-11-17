def powerN(n,x,p):
    if x==0:
        return p
    else:
        p*=n
        return powerN(n,x-1,p)
n=int(input())
x=int(input())
p=1
power=powerN(n,x,p)
print(power)