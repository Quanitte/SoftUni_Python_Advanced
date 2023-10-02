N = int(input())

matrix = [[int(x) for x in input().split(', ')] for _ in range(N)]

primary_diagonal = [matrix[i][i] for i in range(N)]
primary_sum = sum(primary_diagonal)

secondary_diagonal = [matrix[i][N - 1 - i] for i in range(N)]
secondary_sum = sum(secondary_diagonal)

print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {primary_sum}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {secondary_sum}")