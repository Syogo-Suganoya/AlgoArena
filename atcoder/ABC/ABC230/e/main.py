import math

N = int(input())
sqrtN = math.isqrt(N)

# 商が小さい範囲（i > sqrt(N) の場合）
ans = 0
for i in range(1, sqrtN + 1):
    ans += (N // i - N // (i + 1)) * i

# 商が大きい範囲（i = 1 から sqrt(N) まで）
for i in range(1, N // (sqrtN + 1) + 1):
    ans += N // i

print(ans)
