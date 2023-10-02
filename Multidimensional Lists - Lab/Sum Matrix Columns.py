rows, columns = map(int, input().split(', '))
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

for col in range(columns)
    col_sum = sum(matrix[row][col] for row in range(rows))
    print(col_sum)
