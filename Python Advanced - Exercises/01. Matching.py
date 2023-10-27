men_directory, women_directory  = [int(x) for x in input().split()], [int(x) for x in input().split()]
matches = 0
while men_directory and women_directory:
    if women_directory[0] <= 0:
        del women_directory[0]
        continue
    if women_directory[0] % 25 == 0:
        del women_directory[0]
        del women_directory[0]
        continue
    if men_directory[-1] <= 0:
        del men_directory[-1]
        continue
    if men_directory[-1] % 25 == 0:
        del men_directory[-1]
        del men_directory[-1]
        continue
    female = women_directory.pop(0)
    male = men_directory.pop()
    if female == male:
        matches += 1
        continue
    men_directory.append(male - 2)
print(f"Matches: {matches}")
if men_directory:
    print(f"Males left: {', '.join(str(x) for x in reversed(men_directory))}")
else:
    print("Males left: none")
if women_directory:
    print(f"Females left: {', '.join(str(x) for x in women_directory)}")
else:
    print("Females left: none")
