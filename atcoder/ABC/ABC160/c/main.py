K, N = map(int, input().split())
A = list(map(int, input().split()))

# 隣接する家の距離を求める（最後と最初は円環なので K を考慮）
max_gap = 0
for i in range(N - 1):
    max_gap = max(max_gap, A[i + 1] - A[i])
max_gap = max(max_gap, K - (A[-1] - A[0]))

# 答えは円周 - 最大区間
print(K - max_gap)
