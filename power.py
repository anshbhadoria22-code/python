#program to find power of no.without using **
a=int(input("enter a no.: "))
b=int(input("enter its power: "))
ans=1
for i in range(b):
    ans=ans*a
print("power is",ans,end=" ")