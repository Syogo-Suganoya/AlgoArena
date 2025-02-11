N, D = map(int, input().split())
S = input()

count = 0
for i, char in enumerate(reversed(S)):
    if char == "@":
        count += 1
        if count == D:
            index = N - 1 - i

print(S[:index] + "." * (N - index))
