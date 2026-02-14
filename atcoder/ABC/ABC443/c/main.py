N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

last_off = -1
off_total = 0

for x in A:
    if x >= M:
        continue

    if x >= last_off:
        l = x
        r = min(M, x + 100)
        off_total += r - l
        last_off = r

print(M - off_total)
