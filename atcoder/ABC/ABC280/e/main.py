MOD = 998244353


def modinv(a, m=MOD):
    # 拡張ユークリッドでもいいけど、998244353 は素数なので pow を使えば OK
    return pow(a, m - 2, m)


N, P = map(int, input().split())

inv100 = modinv(100)  # 100 の逆元
x = P * inv100 % MOD  # P/100 を mod にした値

p = 1  # p_0 = 1
ans = 1  # a_1 = p_0

for i in range(1, N):
    # p_i = 1 - p_{i-1} * x
    p = (1 - p * x) % MOD
    ans = (ans + p) % MOD

print(ans)
