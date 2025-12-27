N, Q = map(int, input().split())
A = list(map(lambda x: int(x) - 1, input().split()))

queries = [tuple(map(int, input().split())) for _ in range(Q)]

# ダブリングの段数（2^30 > 10^9）
LOG = 30

# next[k][i] : i から 2^k 回後にいる人
# sum[k][i]  : i から 2^k 回分で加算される水量
next_p = [[0] * N for _ in range(LOG)]
sum_p = [[0] * N for _ in range(LOG)]

# 0段目（1回分）
for i in range(N):
    next_p[0][i] = A[i]
    sum_p[0][i] = i + 1  # 人番号は 1-index

# ダブリング構築
for k in range(1, LOG):
    for i in range(N):
        mid = next_p[k - 1][i]
        next_p[k][i] = next_p[k - 1][mid]
        sum_p[k][i] = sum_p[k - 1][i] + sum_p[k - 1][mid]

# クエリ処理
ans = []
for T, B in queries:
    cur = B - 1  # バケツ番号 = 初期の人番号
    water = 0

    for k in range(LOG):
        if (T >> k) & 1:
            water += sum_p[k][cur]
            cur = next_p[k][cur]

    ans.append(water)

# 出力
print("\n".join(map(str, ans)))
