field_size = int(input())
commands = input().split()
field = [input().split() for _ in range(field_size)]

miner_row, miner_col = 0, 0
total_coal = sum(row.count('c') for row in field)
collected_coal = 0
game_over = False

for row_index in range(field_size):
    if 's' in field[row_index]:
        miner_row, miner_col = row_index, field[row_index].index('s')
        break

for command in commands:
    if game_over:
        break

    if command == "left":
        if miner_col > 0:
            miner_col -= 1
    elif command == "right":
        if miner_col < field_size - 1:
            miner_col += 1
    elif command == "up":
        if miner_row > 0:
            miner_row -= 1
    elif command == "down":
        if miner_row < field_size - 1:
            miner_row += 1

    current_position = field[miner_row][miner_col]

    if current_position == "e":
        print(f"Game over! ({miner_row}, {miner_col})")
        game_over = True
    elif current_position == "c":
        collected_coal += 1
        field[miner_row][miner_col] = "*"
        if collected_coal == total_coal:
            print(f"You collected all coal! ({miner_row}, {miner_col})")
            break

if not game_over and collected_coal < total_coal:
    print(f"{total_coal - collected_coal} pieces of coal left. ({miner_row}, {miner_col})")
