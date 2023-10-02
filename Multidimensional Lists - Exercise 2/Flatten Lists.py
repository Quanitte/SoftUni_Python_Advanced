lists = input().split('')
result = []

for sublist in reversed(lists)
    numbers = [int(x) for x in sublist.split() if x]
    result.extend(numbers)

print(result)