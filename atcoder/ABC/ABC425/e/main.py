T, mod = map(int, input().split())

# ================================
# 二項係数 (nCk) を前計算する
# ================================
K = 5010  # 必要な最大サイズ（N の総和が 5000 程度と仮定）

binom = [[0] * K for i in range(K)]
binom[0][0] = 1

# パスカルの三角形を使って nCk を構築
for n in range(1, K):
    binom[n][0] = 1
    for k in range(1, n + 1):
        # nCk = (n-1)C(k-1) + (n-1)Ck
        binom[n][k] = (binom[n - 1][k - 1] + binom[n - 1][k]) % mod


# ================================
# クエリ処理
# ================================
for _ in range(T):
    N = int(input())  # 色の種類数
    C = list(map(int, input().split()))  # 各色ごとの個数

    ans = 1  # 答えを乗算していく形で構築
    s = 0  # これまでに使った合計個数

    # 色ごとに「既に配置された玉の間に新しい玉を挿入する方法」を掛け算していく
    for i in C:
        s += i
        # s 個の並びの中に「i 個の同じ玉」を挿入する方法は sCi
        ans *= binom[s][i]
        ans %= mod

    print(ans % mod)
