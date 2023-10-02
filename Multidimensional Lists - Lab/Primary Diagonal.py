num = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(N)]
diagonal_sum = sum(matrix[i][i] for i in range(N))
print(diagonal_sum)
