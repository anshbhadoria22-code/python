# 5. Take an integer A as input. You have to tell whether A is divisible by both 5 and 11 or not.

A = int(input("enter the number:\n"))
if A%5==0 and A%11==0:
    print("A is divisible by both")
else:
    print("Both condition are not matching")
