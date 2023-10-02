def is_valid_cell(row, col, size):
    return 0 <= row < size and 0 <= col < size

def detonate_bomb(matrix, row, col):
    bomb_value = matrix[row][col]
    if bomb_value > 0:
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if is_valid_cell(r, c, len(matrix)) and matrix[r][c] > 0:
                    matrix[r][c] -= bomb_value
    matrix[row][col] = 0

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
bombs = input().split()

for bomb in bombs:
    bomb_row, bomb_col = map(int, bomb.split(','))
    detonate_bomb(matrix, bomb_row, bomb_col)

alive_cells_count = 0
alive_cells_sum = 0

for row in range(n):
    for col in range(n):
        if matrix[row][col] > 0:
            alive_cells_count += 1
            alive_cells_sum += matrix[row][col]

print(f"Alive cells: {alive_cells_count}")
print(f"Sum: {alive_cells_sum}")

for row in matrix:
    print(" ".join(map(str, row)))
