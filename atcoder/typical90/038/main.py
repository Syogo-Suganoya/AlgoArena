import math

A, B = map(int, input().split())
res = math.lcm(A, B)

res = res if res <= 10**18 else "Large"

print(res)
