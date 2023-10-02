n = int(input())

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

primary_diagonal_sum = sum(matrix[i][i] for i in range(n))
secondary_diagonal_sum = sum(matrix[i][n - i - 1] for i in range(n))
diagonal_difference = abs(primary_diagonal_sum - secondary_diagonal_sum)

print(diagonal_difference)
