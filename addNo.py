num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
addNum=num2
sum=0
while num2>0:
    num2//=10
    sum+=1
ten=10**sum



sum2=num1*ten +addNum

print(sum2)