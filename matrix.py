matrix = [""]
x = int(input("Number of rows: "))
y = int(input("Number of columns: "))

for i in range(x):
    for j in range(y):
        matrix.append(input("> "))

for i in range(x):
    for j in range(y):
        print(matrix[i][j], end = " ")
    print("")


