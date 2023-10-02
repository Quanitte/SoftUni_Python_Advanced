rows, columns = map(int, input().split(', '))
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

max_sum = 0
max_sum_submatrix = []

for row in range(rows - 1):
    for col in range(columns - 1):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
        if current_sum > max_sum:
            max_sum = current_sum
            max_sum_submatrix = [[matrix[row][col], matrix[row][col + 1]], [matrix[row + 1][col], matrix[row + 1][col + 1]]]

print(f'{max_sum_submatrix[0][0]} {max_sum_submatrix[0][1]} ')
print(f'{max_sum_submatrix[1][0]} {max_sum_submatrix[1][1]} ')
print(f'{max_sum}')