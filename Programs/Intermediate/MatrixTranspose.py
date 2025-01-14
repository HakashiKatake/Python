#matrix transpose

list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(list)):
    for j in range(i, len(list[0])):
        list[i][j], list[j][i] = list[j][i], list[i][j]
print(list)