def calculate_eggs(field, N, direction):
    eggs_collected = 0
    collected_positions = []
    x, y = bunny_pos
    
    dx, dy = directions[direction]
    while 0 <= x + dx < N and 0 <= y + dy < N and field[x + dx][y + dy] != 'X':
        x += dx
        y += dy
        if field[x][y].isdigit():
            eggs_collected += int(field[x][y])
            collected_positions.append([x, y])
    
    return eggs_collected, collected_positions

N = int(input())
field = [input().split() for _ in range(N)]

directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
bunny_pos = [(i, row.index('B')) for i, row in enumerate(field) if 'B' in row][0]
max_eggs = 0
best_direction = ''
best_positions = []

for direction in directions:
    eggs, positions = calculate_eggs(field, N, direction)
    if eggs > max_eggs:
        max_eggs = eggs
        best_direction = direction
        best_positions = positions

print(best_direction)
for position in best_positions:
    print(position)
print(max_eggs)
