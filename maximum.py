a=int(input("Enter a number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if(a>b and a>c):
    print("first is maximum")
elif(b>a and b>c):
    print("Second is maximum")
elif(c>a and c>b):
    print("third is maximum")
else:
    print("invalid numbers")