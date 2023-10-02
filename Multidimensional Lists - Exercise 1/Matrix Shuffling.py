def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

rows, columns = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(rows)]

def is_valid(row, col):
    return 0 <= row < rows and 0 <= col < columns

while True:
    command = input().split()
    if command[0] == "END":
        break
    
    if command[0] == "swap" and len(command) == 5:
        row1, col1, row2, col2 = map(int, command[1:])
        if is_valid(row1, col1) and is_valid(row2, col2):
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            print_matrix(matrix)
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
