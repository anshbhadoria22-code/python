A=str(input())
l=A.split()
print(l)
for i in range(len(l)):
    l[i]=l[i][::-1]
print(' '.join(l))