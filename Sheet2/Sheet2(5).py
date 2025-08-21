# 5. Write a program to find the sum of all Natural numbers from 1 to N, where you have to take N as 
# input from user 

N=int(input("Enter a number:"))
sum = 0
for i in range(1,N+1):
    sum+=i
print("The sum of all numbers from 1  to N is : ",sum)