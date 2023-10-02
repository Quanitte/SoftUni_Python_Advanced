N = int(input())

odd_numbers = set()
even_numbers = set()

for i in range(1, N + 1):
    name = input()
    name_value = sum(ord(char) for char in name) // i
    
    if name_value % 2 == 0:
        even_numbers.add(name_value)
    else:
        odd_numbers.add(name_value)

sum_odd_numbers = sum(odd_numbers)
sum_even_numbers = sum(even_numbers)

if sum_odd_numbers == sum_even_numbers:
    print(", ".join(map(str, odd_numbers.union(even_numbers))))
elif sum_odd_numbers > sum_even_numbers:
    print(", ".join(map(str, odd_numbers.difference(even_numbers))))
else:
    print(", ".join(map(str, odd_numbers.symmetric_difference(even_numbers))))
