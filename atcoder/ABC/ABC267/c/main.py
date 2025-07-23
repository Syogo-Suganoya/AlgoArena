N, M = map(int, input().split())
A = list(map(int, input().split()))

# 累積和（部分和をすぐ求めるため）
prefix = [0] * (N + 1)
for i in range(N):
    prefix[i + 1] = prefix[i] + A[i]

# 最初の M 個で重み付き和を計算
cur = 0
for i in range(M):
    cur += (i + 1) * A[i]

ans = cur

# スライディングウィンドウで最大スコアを更新
for i in range(1, N - M + 1):
    # 新しいウィンドウの末尾の値を加算
    # 抜けたウィンドウの値の合計を引く
    cur += M * A[i + M - 1] - (prefix[i + M - 1] - prefix[i - 1])
    ans = max(ans, cur)

print(ans)
