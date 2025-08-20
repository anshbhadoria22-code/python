a=int(input("Enter a number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
sum=a+b+c
if(sum==90):
    print("Angle is Right angle")
elif(sum<90):
    print("Angle is Acute Angle")
elif(sum>90):
    print("Angle isw obutuse angle")
else:
    print("Invalid angles")
