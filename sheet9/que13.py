even_odd_No=lambda x: "even" if x%2==0 else "odd"
num=int(input("Enter a number: "))
print(num,"is",even_odd_No(num))