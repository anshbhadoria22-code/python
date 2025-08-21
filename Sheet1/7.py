# 7. Read three angles of triangles and determine their types(Right triangle, Obtuse triangle, Acute triangle).

# Angle = float(input("enter the angle:\n"))
# if (Angle==90):
#     print("Angle is Right angle")
# elif(Angle<90):
#     print("Angle is Acute angle")
# else:
#     print("Angle is Obtus angle")


# Angle1 = float(input("enter the first angle:\n"))
# Angle2 = float(input("enter the second angle:\n"))
# Angle3 = float(input("enter the third angle:\n"))
# if(Angle1==90 or Angle2==90 or Angle3==90):
#     print("Angle is Right angle")
# elif(Angle1>90 or Angle2>90 or Angle3>90):
#     print("Angle is Obtus angle")
# else:
#     print("Angle is Acute angle")


# age = int(input("Enter age:"))

# if(age>=18):
#     print("Yes!!you are eligible")
# else:
#     print("Sorry!!")


# # 2.
# no = int(input("Enter number to check:"))

# if(no%7==0):
#     print("Yes no is divisible of 7")
# else:
#     print("No")

# # 3.If_Last_NoIS4

# digit =int(input("Enter number to check the last digit:"))
# if digit%3==0 and digit%10==4:
#     print("Yes")

# 5.
# A = int(input("Enter an integer:"))
# if(A%5==0 and A%11==0):
#     print("YES")
# else:
#     print("No")5


# # 6.
# num1=int(input("Enter 1: "))
# num2=int(input("Enter 2: "))
# num3=int(input("Enter 3: "))

# if (num1>num2 and num1>num3):
#     print("Num 1 is greatest",num1)
# elif(num2>num1 and num2>num3):
#     print("Num 2 is greatest",num2)
# else:
#     print("Num 3 is greatest",num3)


a=int(input("Enter 1st side :"))
b= int(input("Enter 2nd side :"))
c=int(input("Enter 3d side :"))

if(a<90 and b<90 and c<90):
    print("It is an acute triangle")
elif(a==90 or b==90 or c==90):
    print("It is an right angled triangle")

else:
    print("It is an abuse triangle")








 