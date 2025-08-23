MOD = 998244353

# 入力
N, K = map(int, input().split())

# 確率を mod で扱うため逆元を使う
invN = pow(N, MOD - 2, MOD)
invN2 = (invN * invN) % MOD
invN1 = pow(N - 1, MOD - 2, MOD)

# 1回の操作で黒が動く確率（位置1→他）
move = (2 * (N - 1) * invN2) % MOD
# 残る確率
stay = (1 - move) % MOD
# 他から位置1に戻る確率
move1 = (move * invN1) % MOD

# dp0: 黒が位置1にいる確率
# dp1: 黒がそれ以外にいる確率
dp0, dp1 = 1, 0

for _ in range(K):
    ndp0 = (dp0 * stay + dp1 * move1) % MOD
    ndp1 = (dp0 * move + dp1 * (1 - move1)) % MOD
    dp0, dp1 = ndp0, ndp1

# 期待値を計算
# sum_{i=2..N} i = (N+2)*(N-1)//2
total = (N + 2) * (N - 1) // 2
total %= MOD

# 期待値 = 1*dp0 + (total/(N-1)) * dp1
invN1 = pow(N - 1, MOD - 2, MOD)
expect = (dp0 + dp1 * total % MOD * invN1) % MOD

print(expect)
