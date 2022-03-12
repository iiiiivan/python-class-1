l=[
    [5, 6, 7, 8,],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [1, 2, 3, 4],
    ]

max_l=0
for i in range(4):
    for j in range(4):
        l[i][j] *= -1
        l[i][j] -= 100


print(l)

max_l=l[0][0]
for i in range(4):
    for j in range(4):
        if l[i][j]>max_l:
            max_l=l[i][j]

print(max_l)