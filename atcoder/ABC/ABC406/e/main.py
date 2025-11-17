# 998244353 を使うので modint と同様の振る舞いを自前で実装
MOD = 998244353


# 冪乗を高速にとる関数
def mod_pow(a, b, mod=MOD):
    res = 1
    while b > 0:
        if b & 1:
            res = res * a % mod
        a = a * a % mod
        b >>= 1
    return res


N = 60

# c[i][j]: 0 <= x < 2^i で popcount(x)=j の個数
# s[i][j]: 同じ条件で「x の総和」
c = [[0] * (N + 1) for _ in range(N + 1)]
s = [[0] * (N + 1) for _ in range(N + 1)]


def preset():
    """c[i][j], s[i][j] を前計算するパート"""
    c[0][0] = 1
    for i in range(N):
        for j in range(i + 1):
            # 1 を置く場合（popcount が +1）
            c[i + 1][j + 1] = (c[i + 1][j + 1] + c[i][j]) % MOD
            s[i + 1][j + 1] = (s[i + 1][j + 1] + s[i][j]) % MOD
            # i ビット目を 1 にすると、その桁は 2^i を寄与する
            s[i + 1][j + 1] = (s[i + 1][j + 1] + c[i][j] * mod_pow(2, i)) % MOD

            # 0 を置く場合（popcount 増えない）
            c[i + 1][j] = (c[i + 1][j] + c[i][j]) % MOD
            s[i + 1][j] = (s[i + 1][j] + s[i][j]) % MOD


def solve(n, k):
    """
    0 <= x <= n かつ popcount(x)=k のときの x の総和を求める。

    C++ 版と同じく、n を上位ビットから 1 本ずつ見下ろして、
    「そのビットを 0 にする場合に貢献する x の総和」を加算していく。
    """
    a = [(n >> i) & 1 for i in range(N)]  # 下位ビットから配列化
    cur = 0  # これまで確定した x の popcount
    offset = 0  # これまで確定した x のプレフィックス値
    ans = 0

    # 上位ビット（59）→ 下位（0）へ
    for i in range(N - 1, -1, -1):
        if a[i] == 1:
            # このビットを 0 とする場合、
            # 残りの popcount は k - cur 必要
            if cur <= k:
                need = k - cur
                ans = (ans + s[i][need]) % MOD  # i 未満の x の総和
                ans = (ans + offset * c[i][need]) % MOD  # prefix を付けた分
            # このビットを 1 として進む
            cur += 1
            offset = (offset + mod_pow(2, i)) % MOD

    # すべて n と同じビット配置で cur==k なら n 自身を加算
    if cur == k:
        ans = (ans + offset) % MOD

    return ans


# ---- main ----
preset()
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))
