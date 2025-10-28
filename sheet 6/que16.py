A=str(input())
con=A+A
print(con)
for i in con:
    if i.isupper():
        con=con.replace(i,'')
    elif i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        con=con.replace(i,'#')
print(con)