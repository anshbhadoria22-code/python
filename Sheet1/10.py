# 10. WAP to accept a number from 1 to 7 and display the name of the day, like 1 for Sunday, 2 for Monday, etc.

# USING LISTS:

days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
num = int(input("Enter a number (1-7): "))
print(days[num-1] if 1 <= num <= 7 else "Invalid input! Enter 1-7.")
 
