input_string = input()
size = int(input())
game_matrix, player_row, player_col = [], 0, 0
for row_ in range(size):
    game_matrix.append(list(input()))
    if "P" in game_matrix[row_]:
        player_row, player_col = row_, game_matrix[row_].index("P")
        game_matrix[player_row][player_col] = "-"
number_of_commands = int(input())
for com in range(number_of_commands):
    command = input()
    temp_row, temp_col = player_row, player_col
    if command == "up":
        temp_row -= 1
    elif command == "down":
        temp_row += 1
    elif command == "left":
        temp_col -= 1
    elif command == "right":
        temp_col += 1
    if not 0 <= temp_row < size or not 0 <= temp_col < size:
        input_string = input_string[:-1]
        continue
    player_row, player_col = temp_row, temp_col
    step_on = game_matrix[player_row][player_col]
    if step_on != "-":
        game_matrix[player_row][player_col] = "-"
        input_string += step_on
game_matrix[player_row][player_col] = "P"
print(input_string)
[print(*row, sep="") for row in game_matrix]