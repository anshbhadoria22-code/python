# 10. You are given an integer A as input, and you need to determine whether it is a palindrome 
# or not. A palindrome integer is one whose digits, when reversed, result in the same number. 
# For example, 121 is a palindrome because its reverse is also 121, but 123 is not a palindrome 
# because its reverse is 321.Note: The given integer will not have any leading zeros. 


N=int(input("Enter a number:"))
original=N
rev=""
while N>0:
    rem=N%10
    rev+=str(rem)
    N=N//10
print("Yes the number is palindrome!" if original==int(rev) else "No the number is not a plaindrome!")