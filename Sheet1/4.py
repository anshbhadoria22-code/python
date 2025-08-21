# 4. WAP to check if the number is divisible by 7 or if the last digit is 5. 

Number = float(input("enter the number:\n"))
if Number%7==0 and Number%10==5:
    print("Yes,all condition are true")
else:
    print("No,both condition are not matching")