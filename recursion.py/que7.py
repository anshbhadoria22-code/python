def revstr(s,n):
    if n==0:
        return
    else:
        print(s[n-1],end="")
        revstr(s,n-1)
s=str(input())
n=len(s)
revstr(s,n)