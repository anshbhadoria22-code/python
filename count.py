number=int(input("enter a number: "))
digit=int(input("enter a digit: "))
count=0
while (number>0):
    last_digit=number%10
    if (last_digit==digit):
        count+=1
    number//10
print(count)