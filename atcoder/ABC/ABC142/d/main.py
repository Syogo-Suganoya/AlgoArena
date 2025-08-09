import math

A, B = map(int, input().split())
g = math.gcd(A, B)

cnt = 0
i = 2
while i * i <= g:
    if g % i == 0:
        cnt += 1
        while g % i == 0:
            g //= i
    i += 1
if g > 1:
    cnt += 1

print(cnt + 1)  # 1 を含めて
