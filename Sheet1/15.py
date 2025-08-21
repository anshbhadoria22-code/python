# 15. Accept the percentage from the user and display the grade according to the following 
# criteria. 
# ● 
# Below 25 – D 
# ● 
# 25 to 45 – C 
# ● 
# 45 to 65 – B 
# ● 
# 65 to 85 – A 
# ● 
# Above 85 – A+ 


percentage = float(input("Enter your percentage:\n"))

if percentage < 25:
    print("Your grade is: D")
elif percentage <= 45:
    print("Your grade is: C")
elif percentage <= 65:
    print("Your grade is: B")
elif percentage <= 85:
    print("Your grade is: A")
else:
    print("Your grade is: A+")