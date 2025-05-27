N = int(input())

MOD = 998244353  # 余りを取るための定数


def modinv(a):
    # aの逆元をMODで計算する（フェルマーの小定理を利用）
    # a^(MOD-2) ≡ a^(-1) mod MOD
    return pow(a, MOD - 2, MOD)


d = len(str(N))  # Nの桁数を求める

# 10のd乗（例: d=2のとき100）をMODで取る
pow10d = pow(10, d, MOD)

# 等比数列の分子：10^(d*N) - 1
# 先に+MODしておくことで負数にならないようにする
numerator = (pow(pow10d, N, MOD) - 1 + MOD) % MOD

# 等比数列の分母の逆元：10^d - 1 の逆元
denominator_inv = modinv(pow10d - 1)

# 等比数列の和：(10^(d*N)-1)/(10^d-1) をMODで計算
# さらにNを掛ける（NがN回繰り返されているから）
result = N * numerator % MOD
result = result * denominator_inv % MOD

print(result)
