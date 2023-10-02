N = int(input())
petrol_pumps = []

for _ in range(N):
    petrol, distance = map(int, input().split())
    petrol_pumps.append((petrol, distance))

start = 0
current_petrol = 0
total_petrol = 0
total_distance = 0

for i in range(N):
    petrol, distance = petrol_pumps[i]
    current_petrol += petrol - distance
    total_petrol += petrol
    total_distance += distance

    if current_petrol < 0:
        current_petrol = 0
        start = i + 1

if total_petrol >= total_distance:
    print(start)
else:
    print(-1)
