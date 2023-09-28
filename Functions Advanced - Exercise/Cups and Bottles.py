cups_capacity = list(map(int, input().split()))
bottles = list(map(int, input().split()))

wasted_water = 0
remaining_cups = []

while cups_capacity and bottles:
    current_cup = cups_capacity[0]
    current_bottle = bottles.pop()

    if current_bottle >= current_cup:
        wasted_water += current_bottle - current_cup
        cups_capacity.pop(0)
    else:
        cups_capacity[0] -= current_bottle

if not cups_capacity:
    print(f"Bottles: {' '.join(map(str, bottles[::-1]))}")
else:
    print(f"Cups: {' '.join(map(str, cups_capacity))}")

print(f"Wasted litters of water: {wasted_water}")
