# 9. Take an integer N as input. Your task is to calculate and print the sum of the digits of the 
# given number N.


N = int(input("Enter a number:\n"))
sumofdigits = 0
while N != 0:
    digit = N % 10        
    sumofdigits += digit   
    N = N // 10           

print("Sum of digits:", sumofdigits)