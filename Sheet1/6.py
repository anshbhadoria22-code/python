# 6. Read three integers and print their maximum. 

A = float(input("enter the first number:\n"))
B = float(input("enter the second number:\n"))
C = float(input("enter the third number:\n"))
if(A>B and A>C):
    print("A is greatest")
elif(B>A and B>C):
    print("B is greatest")
else:
    print("C is greatest")