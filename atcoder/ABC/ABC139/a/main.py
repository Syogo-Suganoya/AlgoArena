S = input()
T = input()

res = 0
for s, t in zip(S, T, strict=True):
    if s == t:
        res += 1

print(res)
