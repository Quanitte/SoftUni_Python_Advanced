from collections import deque
customer_queue = deque()
while True:
    command = input()
    if command == "End":
        remaining_count = len(customer_queue)
        print(f"{remaining_count} people remaining.")
        break
    elif command == "Paid":
        while customer_queue:
            print(customer_queue.popleft())
    else:
        customer_queue.append(command)