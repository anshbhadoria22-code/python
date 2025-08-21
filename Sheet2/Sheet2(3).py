# 3. Write a program to print all even numbers from 1 to N, where you have to take N as input 
# from the user.

N = int(input("Enter a number: "))
for x in range(1, N+1):
    if (x%2==0):
        print(x,end=" ")