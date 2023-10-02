N = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(N)]

while True:
    command = input()
    if command == "END":
        break

    command, row, col, value = command.split()
    row, col, value = int(row), int(col), int(value)

    if 0 <= row < N and 0 <= col < len(matrix[0]):
        if command == "Add":
            matrix[row][col] += value
        elif command == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

for row in matrix:
    print(*row)
