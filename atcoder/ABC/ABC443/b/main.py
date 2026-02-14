N, M = map(int, input().split())

now = 0
y = 0
be = N

while now < M:
    now += be
    be += 1
    y += 1

print(y - 1)
