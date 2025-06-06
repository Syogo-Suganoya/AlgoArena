H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

# まず全マスの最小値を求める
min_val = min(min(row) for row in A)

# すべてのマスをmin_valにするために必要な操作回数を数える
res = 0
for i in range(H):
    for j in range(W):
        res += A[i][j] - min_val  # 各マスから最小値を引いた差分を加算

print(res)
