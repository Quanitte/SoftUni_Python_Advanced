rows, columns = map(int, input().split())

def generate_palindrome(row, col):
    first_letter = chr(ord('a') + row)
    middle_letter = chr(ord('a') + row + col)
    return f"{first_letter}{middle_letter}{first_letter}"

matrix = [[generate_palindrome(row, col) for col in range(columns)] for row in range(rows)]

for row in matrix:
    print(" ".join(row))
