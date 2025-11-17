def pal(s,n,newS):
    if (n==0):
        return newS
    else:
        newS+=s[n-1]
        return pal(s,n-1,newS)

a=str(input())
n=len(a)
newS=""
newS=(pal(a,n,newS))
if(newS==a):
    print("is palindrome")
else:
    print("not a plaindrome")