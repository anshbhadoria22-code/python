# 6. You are given an integer A, you need to find and return the sum of all the even numbers 
# between 1 and A. Even numbers are those numbers that are divisible by 2. 

N=int(input("Enter a number:"))
sum=0
for i in range(1,N+1):
    if i%2==0:
        sum+=i
print("The sum of all even numbers is ",sum)