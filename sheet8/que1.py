import math
def sqRoot(n):
    root=math.sqrt(n)
    if root.is_integer():
        print(int(root))
    else:
        print(-1)
n=int(input())
sqRoot(n)
