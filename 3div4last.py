num= int(input("Enter a number: "))
if(num%3==0):
    if(num%10==4):
        print("number is divisible by 4 and last digit is 3")
else:
    print("invalid number")