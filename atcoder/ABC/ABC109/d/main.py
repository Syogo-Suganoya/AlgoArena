N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

moves = []

for i in range(N):
    for j in range(M):
        if A[i][j] % 2 == 1:  # 奇数なら
            if j + 1 < M:  # 右に渡せる
                A[i][j] -= 1
                A[i][j + 1] += 1
                moves.append((i + 1, j + 1, i + 1, j + 2))
            elif i + 1 < N:  # 下に渡せる
                A[i][j] -= 1
                A[i + 1][j] += 1
                moves.append((i + 1, j + 1, i + 2, j + 1))

# 出力
print(len(moves))
for move in moves:
    print(*move)
