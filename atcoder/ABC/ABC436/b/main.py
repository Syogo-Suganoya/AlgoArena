N = int(input())

magic = [[0] * N for _ in range(N)]
r = 0
c = (N - 1) // 2

magic[r][c] = 1

for k in range(2, N * N + 1):
    nr = (r - 1) % N
    nc = (c + 1) % N
    if magic[nr][nc] != 0:
        r = (r + 1) % N
    else:
        r = nr
        c = nc

    magic[r][c] = k

for row in magic:
    print(*row)
