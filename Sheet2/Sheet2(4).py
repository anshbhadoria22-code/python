 
# 4. Write a program to print all odd numbers from 1 to N, where you have to take N as input 
# from user. 

N = int(input("Enter a number:\n"))
print("Odd no.from 1 to", N, "are:")
for i in range(1, N+1):
    if i % 2 != 0:   
        print(i, end=" ")