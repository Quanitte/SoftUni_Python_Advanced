starting_water = int(input())
people_queue = []
while True:
    command = input()
    if command == "Start":
        break
    people_queue.append(command)
while True:
    command = input()
    if command == "End":
        break
    if command.startswith("refill"):
        _, liters = command.split()
        liters_to_add = int(liters)
        starting_water += liters_to_add
    else:
        liters_needed = int(command)
        if liters_needed <= starting_water:
            person = people_queue.pop(0)
            starting_water -= liters_needed
            print(f"{person} got water")
        else:
            person = people_queue.pop(0)
            print(f"{person} must wait")

print(f"{starting_water} liters left")