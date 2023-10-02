numbers = input().split()
number_counts = {}

for number in numbers:
    number = float(number)
    if number not in number_counts:
        number_counts[number] = 1
    else:
        number_counts[number] += 1

for number, count in number_counts.items():
    formatted_number = format(number, ".1f")
    print(f"{formatted_number} - {count} times")
