rows, columns = map(int, input().split())
snake = input()

matrix = [[0] * columns for _ in range(rows)]
current_char_index = 0

for row in range(rows):
    if row % 2 == 0:
        for col in range(columns):
            matrix[row][col] = snake[current_char_index]
            current_char_index = (current_char_index + 1) % len(snake)
    else:
        for col in range(columns - 1, -1, -1):
            matrix[row][col] = snake[current_char_index]
            current_char_index = (current_char_index + 1) % len(snake)

for row in matrix:
    print("".join(row))
