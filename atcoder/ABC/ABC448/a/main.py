N, M = map(int, input().split())
A = list(map(int, input().split()))

for a in A:
    if a < M:
        print(1)
        M = a
    else:
        print(0)
