# 3. WAP to check if the number is divisible by 3 and the last digit is 4.

Number  = float(input("enter the number:\n"))
if Number%3==0 and Number%10==4:
    print("Yes,all condition are true")
else:
    print("NO,both condition are not matching")