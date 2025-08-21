# 12. You are given 3 integer angles(in degrees), A, B, and C, of a triangle. You have to tell whether the triangle is valid or not. A triangle is valid if the sum of its angles equals 180.

A =int(input("enter the first angle:\n"))
B =int(input("enter the second angle:\n"))
C =int(input("enter the third angle:\n"))

if A > 0 and B > 0 and C > 0 and (A + B + C == 180):
    print("The triangle is valid")
else:
    print("The triangle is not valid")