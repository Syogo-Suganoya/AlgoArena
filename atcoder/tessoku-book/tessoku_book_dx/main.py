S = input()
stack = []

for i, ch in enumerate(S):
    if ch == "(":
        stack.append(i)
    elif ch == ")":
        if stack:
            open_idx = stack.pop()
            print(open_idx + 1, i + 1)
