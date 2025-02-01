N = int(input())

s = set()
for _ in range(N):
    S = input()
    if S[::-1] not in s:
        s.add(S)

print(len(s))
