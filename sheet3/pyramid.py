num = int(input("enter the number: "))

for i in range(num):
    print("_ " * (num - i - 1), end="")
    print("* " * (i + 1))