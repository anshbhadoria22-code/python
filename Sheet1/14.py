# 14. Write a program to input three numbers(A, B & C) from the user and print the minimum element among A, B & C.

A = int(input("Enter first number:\n "))
B = int(input("Enter second number:\n "))
C = int(input("Enter third number:\n "))

if A <=B and A < C:
    print("A is minimum")
elif B < A and B < C:
    print("B is minimum")
else:
    print("C is minimum")
