rows = 5
width = rows * 2

for i in range(rows):
    for j in range(width):
        if j < rows - i or j >= rows +i:
            print('*', end='')
        else:
            print(' ', end='')
    print()