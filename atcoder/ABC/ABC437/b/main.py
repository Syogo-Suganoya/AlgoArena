H, W, N = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(H)]

B = set()
for _ in range(N):
    B.add(int(input()))

res = 0

for i in range(H):
    tmp = 0
    for j in range(W):
        if maze[i][j] in B:
            tmp += 1
    res = max(res, tmp)

print(res)
