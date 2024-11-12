# 公式解説をpyに置換
# https://atcoder.jp/contests/abc379/editorial/11323

N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))

xa = {}

for i in range(M):
    xa[X[i]] = A[i]

xa = sorted(xa.items(), key=lambda item: item[0])

sum_a = 0
sum_idx = 0

# 計算ループ
for x, a in xa:
    if sum_a < x - 1:
        print(-1)
        exit(0)
    sum_a += a
    sum_idx += a * x

# 最終条件のチェック
if sum_a != N:
    print(-1)
else:
    print(N * (N + 1) // 2 - sum_idx)
