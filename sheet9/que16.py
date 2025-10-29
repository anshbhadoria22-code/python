def fun(a):
    return True if a % 2 == 0 else False
sequence=[1,4,5,7,7.5,5.4,3,6]
def filter(sequence):
    filtered=[]
    for i in sequence:
        if fun(i)==True:
            filtered.append(i)
    print(filtered)

filter(sequence)
            