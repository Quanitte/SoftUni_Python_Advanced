ocean_size = int(input())
directions = {"right": (0, 1), "left": (0, -1), "up": (-1, 0), "down": (1, 0)}
lives, enemy_cruisers, ocean_grid, submarine_row, submarine_col = 2, [], [], 0, 0
for x in range(ocean_size):
    ocean_grid.append(list(input()))
    if "S" in ocean_grid[x]:
        submarine_row, submarine_col = x, ocean_grid[x].index("S")
        ocean_grid[submarine_row][submarine_col] = "-"
    if "C" in ocean_grid[x]:
        [enemy_cruisers.append([x, i]) for i in range(ocean_size) if "C" == ocean_grid[x][i]]
while enemy_cruisers:
    if lives < 0:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine_row}, {submarine_col}]!")
        break
    row_to_add, col_to_add = directions[input()]
    submarine_row, submarine_col = submarine_row + row_to_add, submarine_col + col_to_add
    if ocean_grid[submarine_row][submarine_col] == "*":
        lives -= 1
    elif ocean_grid[submarine_row][submarine_col] == "C":
        enemy_cruisers.remove([submarine_row, submarine_col])
    ocean_grid[submarine_row][submarine_col] = "-"
else:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
ocean_grid[submarine_row][submarine_col] = "S"
[print(*row, sep="") for row in ocean_grid]
