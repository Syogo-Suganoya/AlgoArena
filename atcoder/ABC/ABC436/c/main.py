N, M = map(int, input().split())

s = set()
res = 0

for _ in range(M):
    A, B = map(int, input().split())

    cells = [(A, B), (A + 1, B), (A, B + 1), (A + 1, B + 1)]

    if any(p in s for p in cells):
        continue

    for p in cells:
        s.add(p)
    res += 1

print(res)
