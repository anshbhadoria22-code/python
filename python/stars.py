# n=int(input("enter a number: "))
# for i in range(0,n):
#     print("*",end=" ")


#2nd star
# a=int(input("enter a rows: "))
# b=int(input("enter no. of stars: "))
# for i in range(0,a):
#     for j in range(0,b):
#         print("*",end=" ")
#     print("")

#3rd stars
# a=int(input("enter a rows: "))
# for i in range(1,a+1):
#     for j in range(i):
#          print("*",end=" ")
#     print(" ")

   #4 star
a=int(input("enter a rows: "))
for i in range(1,a+1):
    for j in range(a,i-1,-1):
              print("*",end=" ")
    print(" ")