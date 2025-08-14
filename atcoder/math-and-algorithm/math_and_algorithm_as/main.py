MOD = 10**9 + 7


def modinv(a, m):
    return pow(a, m - 2, m)


def solve(N):
    # 4^(N+1) % MOD を計算
    power = pow(4, N + 1, MOD)
    # (4^(N+1) - 1) % MOD を計算
    numerator = (power - 1 + MOD) % MOD
    # 3 の逆元を計算
    denominator_inv = modinv(3, MOD)
    # 結果を計算
    result = numerator * denominator_inv % MOD
    return result


# 入力を受け取る
N = int(input())
print(solve(N))
