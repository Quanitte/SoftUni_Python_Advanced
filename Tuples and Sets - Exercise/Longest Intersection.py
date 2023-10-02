N = int(input())
longest_intersection = set()

for _ in range(N):
    first_range, second_range = input().split("-")
    first_start, first_end = map(int, first_range.split(","))
    second_start, second_end = map(int, second_range.split(","))
    current_intersection = set(range(first_start, first_end + 1)).intersection(range(second_start, second_end + 1))

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

longest_intersection_numbers = ", ".join(map(str, longest_intersection))
length_longest_intersection = len(longest_intersection)

print(f"Longest intersection is [{longest_intersection_numbers}] with length {length_longest_intersection}")
