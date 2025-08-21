# Take a number A as input, print its multiplication table having the first 10 multiples.

N = int(input("Enter a number:\n"))

print("Table of:", N)
for i in range(1, 11):   
    print(N, "x", i, "=", N* i)