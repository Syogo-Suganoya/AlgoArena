MOD = 998244353

N = int(input().rstrip())

# 条件を整理すると：
# 1 ≤ a, b, c ≤ N, a % b = c, かつ a, b, c は全て異なる
# → 首尾として b > c（余りは b より小さい）かつ a > b （a = b だと余り c=0 か b→a=c になり異なり条件と食い違う）という構図になる。
#
# 結局、「(b, a) の組で、1 ≤ b < a ≤ N」であって、かつ「a % b ≠ 0」を満たすものの個数を数えるのが主眼。
#
# 全事象：b < a ≤ N の組 = Σ_{a=1..N} (a−1) = N(N−1)/2
# 余事象：a % b = 0 かつ b < a ≤ N の組。これは Σ_{b=1..N} (⌊N/b⌋ − 1)（a = b の分を除く）で求まる。
#
# よって答え = 全事象 − 余事象
#          = N(N−1)/2 − Σ_{b=1..N}(⌊N/b⌋ − 1)
#          = N(N−1)/2 − (Σ_{b=1..N}⌊N/b⌋) + N
#
# ただし N が最大 10^12 なので Σ_{b=1..N}⌊N/b⌋ を直接ループで取るのは無理。
# 商列挙（＝ floor sum の高速計算）を用して O(√N) 程度で求める。

# 全事象 = N*(N−1)//2 mod MOD
total = N * (N - 1) // 2 % MOD

# Σ_{b=1..N} ⌊N/b⌋ を計算（商列挙）
sum_floor = 0
b = 1
while b <= N:
    q = N // b
    # 商 q を持つ b の範囲は b .. N//q
    last = N // q
    # この範囲の b の個数は (last − b + 1)
    sum_floor = (sum_floor + q * (last - b + 1)) % MOD
    b = last + 1

# 余事象 = Σ(⌊N/b⌋ − 1) = sum_floor − N
extra = (sum_floor - N) % MOD

ans = (total - extra + MOD) % MOD
print(ans)
