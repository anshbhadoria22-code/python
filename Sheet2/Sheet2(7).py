# 7. Take an integer A as input. You have to print the sum of all odd numbers in the range [1, A].


N = int(input("Enter a number: "))
sumofodd = 0
for i in range(1, N+1):   
    if i % 2 != 0:       
        sumofodd += i
print("Sum of all odd numbers from 1 to", N, "is:", sumofodd)

