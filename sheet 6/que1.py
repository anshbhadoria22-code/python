T=str(input("enter a string: "))
vowels=0
cons=0
if T.isdigit():
    pass
else:
   for i in T:
      if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U"):
        vowels=vowels+1
      else:
        cons=cons+1
   print(vowels,cons)        
