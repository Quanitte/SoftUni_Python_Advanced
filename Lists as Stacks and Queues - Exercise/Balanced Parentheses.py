expression = input()
stack = []
brackets = {')': '(', '}': '{', ']': '['}

for char in expression:
    if char in '({[':
        stack.append(char)
    elif char in ')}]':
        if not stack or stack[-1] != brackets[char]:
            print("NO")
            break
        stack.pop()
else:
    print("YES" if not stack else "NO")
