rows, columns = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(rows)]

max_sum = float('-inf')
max_square = []

for row in range(rows - 2):
    for col in range(columns - 2):
        square_sum = sum(matrix[row][col:col + 3]) + sum(matrix[row + 1][col:col + 3]) + sum(matrix[row + 2][col:col + 3])
        if square_sum > max_sum:
            max_sum = square_sum
            max_square = [matrix[row][col:col + 3], matrix[row + 1][col:col + 3], matrix[row + 2][col:col + 3]]

print(f"Sum = {max_sum}")
for row in max_square:
    print(" ".join(map(str, row)))
