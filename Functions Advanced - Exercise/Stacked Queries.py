stack = []
max_stack = []
min_stack = []
n = int(input())
for _ in range(n):
    query = input().split()
    command = int(query[0])
    if command == 1:
        number = int(query[1])
        stack.append(number)

        if not max_stack or number >= max_stack[-1]:
            max_stack.append(number)

        if not min_stack or number <= min_stack[-1]:
            min_stack.append(number)
    elif command == 2:
        if stack:
            if stack[-1] == max_stack[-1]:
                max_stack.pop()
            if stack[-1] == min_stack[-1]:
                min_stack.pop()
            stack.pop()
    elif command == 3:
        if max_stack:
            print(max_stack[-1])
    elif command == 4:
        if min_stack:
            print(min_stack[-1])
stack_str = ', '.join(map(str, reversed(stack)))
print(stack_str)
