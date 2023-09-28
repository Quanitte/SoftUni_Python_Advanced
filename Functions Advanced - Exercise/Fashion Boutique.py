clothes = list(map(int, input().split()))
rack_capacity = int(input())
racks = 0
current_rack_sum = 0
for cloth in reversed(clothes):
    if current_rack_sum + cloth <= rack_capacity:
        current_rack_sum += cloth
    else:
        racks += 1
        current_rack_sum = cloth
if current_rack_sum > 0:
    racks += 1
print(racks)
