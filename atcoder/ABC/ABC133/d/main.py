N = int(input())
A = list(map(int, input().split()))

# ダムに溜まる総水量 S
S = sum(A)

# 偶数インデックスのみを足して2倍した総和（A[1], A[3], ...）
sum_even_idx = sum(A[i] for i in range(1, N, 2))

# X1 を導出
X = [0] * N
X[0] = S - 2 * sum_even_idx

# 漸化式を使って順に計算
for i in range(N - 1):
    X[i + 1] = 2 * A[i] - X[i]

# 結果出力
print(*X)
