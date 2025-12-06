MOD = 10**9 + 7


# 階乗・逆元階乗を前計算する関数
def prepare_factorials(n):
    fact = [1] * (n + 1)  # n! を格納
    invfact = [1] * (n + 1)  # (n!)^{-1} を格納

    # 階乗を計算（1 から順に）
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD

    # フェルマーの小定理で逆元を計算
    invfact[n] = pow(fact[n], MOD - 2, MOD)

    # 逆元階乗を逆方向に計算
    for i in range(n, 0, -1):
        invfact[i - 1] = invfact[i] * i % MOD

    return fact, invfact


# nCr を計算
def comb(n, r, fact, invfact):
    if r < 0 or r > n:
        return 0
    return fact[n] * invfact[r] % MOD * invfact[n - r] % MOD


# ------------------------------
# メイン処理
# ------------------------------
N, K = map(int, input().split())
A = list(map(int, input().split()))

# ソート（max と min の位置関係を固定するため）
A.sort()

# 階乗前計算（最大 N まで）
fact, invfact = prepare_factorials(N)

max_sum = 0
min_sum = 0

# ------------------------------
# 1. max(S) の総和
# A[i] が最大値になるためには、
#   残り K-1 を A[0..i-1] の i 個から選ぶ
# → 選び方は C(i, K-1)
# ------------------------------
for i in range(K - 1, N):
    c = comb(i, K - 1, fact, invfact)
    max_sum = (max_sum + A[i] * c) % MOD

# ------------------------------
# 2. min(S) の総和
# A[i] が最小値になるためには、
#   残り K-1 を A[i+1..N-1] の N-i-1 個から選ぶ
# → 選び方は C(N-i-1, K-1)
# ------------------------------
for i in range(0, N - (K - 1)):
    c = comb(N - i - 1, K - 1, fact, invfact)
    min_sum = (min_sum + A[i] * c) % MOD

# ------------------------------
# 結果
# (最大値総和 - 最小値総和)
# ------------------------------
print((max_sum - min_sum) % MOD)
