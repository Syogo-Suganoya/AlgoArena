MOD = 10**9 + 7

N = int(input())

# N と N+1 の積を計算し、2 で割るために逆元を使用
sum_N = N * (N + 1) // 2
sum_N %= MOD

# 結果を二乗し、MOD で剰余を取る
result = sum_N * sum_N % MOD

print(result)
