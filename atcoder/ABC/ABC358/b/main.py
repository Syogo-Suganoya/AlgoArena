N, M = map(int, input().split())
A = list(map(int, input().split()))

now = -1
for a in A:
    now = max(now, a)
    now += M
    print(now)
