n = int(input())
d = [[0] * n for _ in range(n)]

# 距離行列の入力（上三角部分のみ）
for i in range(n - 1):
    line = list(map(int, input().split()))
    for j in range(i + 1, n):
        d[i][j] = line[j - i - 1]
        d[j][i] = line[j - i - 1]  # 対称行列にする

# dp[mask] : mask で表される頂点の集合に対する最大距離和
dp = [0] * (1 << n)

for b in range((1 << n) - 1):
    # mask b に含まれない最初の頂点 l を探す
    l = -1
    for i in range(n):
        if not (b >> i) & 1:
            l = i
            break
    if l == -1:
        continue  # 全て選ばれていれば次へ

    # l とペアにできる i を探す
    for i in range(n):
        if (b >> i) & 1 or i == l:
            continue
        nb = b | (1 << l) | (1 << i)  # 新しいマスク
        dp[nb] = max(dp[nb], dp[b] + d[l][i])

print(dp[(1 << n) - 1])
