input_string = input()
integers = list(map(int, input_string.split()))
stack = []
for num in integers:
    stack.append(num)
reversed_integers = []
while stack:
    reversed_integers.append(stack.pop())
print(" ".join(map(str, reversed_integers)))
