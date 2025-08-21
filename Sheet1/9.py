# 9. WAP to check whether a year is a leap year or not. 
Year = int(input("Enter the year:\n"))
if (Year % 400 == 0) or (Year % 4 == 0 and Year % 100 != 0):
    print("Year is Leap year.")
else:
    print("Year is not Leap.")