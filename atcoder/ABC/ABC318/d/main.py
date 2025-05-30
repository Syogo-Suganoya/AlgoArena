N = int(input())
D = [[0] * N for _ in range(N)]
for i in range(N):
    row = list(map(int, input().split()))
    for j, val in enumerate(row):
        D[i][i + j + 1] = val
        D[i + j + 1][i] = val

dp = [0] * (1 << N)
for S in range(1 << N):
    # 未使用の最小の頂点を探す
    for i in range(N):
        if not (S >> i) & 1:
            break
    else:
        continue  # すべての頂点が使用済み

    for j in range(i + 1, N):
        if not (S >> j) & 1:
            T = S | (1 << i) | (1 << j)
            dp[T] = max(dp[T], dp[S] + D[i][j])

print(dp[(1 << N) - 1])
