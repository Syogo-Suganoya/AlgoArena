import math

N, A, B = map(int, input().split())

# ステップ 1: 全体の和
total = N * (N + 1) // 2

# ステップ 2: A の倍数の総和
kA = N // A
sumA = A * kA * (kA + 1) // 2

# ステップ 3: B の倍数の総和
kB = N // B
sumB = B * kB * (kB + 1) // 2

# ステップ 4: A と B 両方の倍数（最小公倍数 L）
L = A * B // math.gcd(A, B)
kL = N // L
sumL = L * kL * (kL + 1) // 2

# 包除原理を適用して答えを得る
result = total - sumA - sumB + sumL
print(result)
