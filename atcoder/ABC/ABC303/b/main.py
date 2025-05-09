N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

# 全体のペアの数：N個の中から2つ選ぶ組み合わせ
c = N * (N - 1) // 2

# 順序を保って隣接のペアを set に登録していく
b = set()
for i in range(M):
    for j in range(1, N):
        a, b_ = sorted((A[i][j], A[i][j - 1]))
        b.add((a, b_))

# 競合が発生したペアの数を差し引く
print(c - len(b))
