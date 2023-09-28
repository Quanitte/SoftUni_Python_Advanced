kids = input().split()
n = int(input())
circle = kids
while len(circle) > 1:
    index_to_remove = (n - 1) % len(circle)
    removed_kid = circle.pop(index_to_remove)
    print(f"Removed {removed_kid}")
    circle = circle[index_to_remove:] + circle[:index_to_remove]
print(f"Last is {circle[0]}")