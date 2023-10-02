n = int(input())
students = {}

for _ in range(n):
    name, grade = input().split()
    grade = float(grade)
    if name in students:
        students[name].append(grade)
    else:
        students[name] = [grade]

for name, grades in sorted(students.items()):
    average_grade = sum(grades) / len(grades)
    formatted_grades = " ".join(map(str, grades))
    print(f"{name} -> {formatted_grades} (avg: {average_grade:.2f})")
