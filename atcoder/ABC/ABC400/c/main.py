import math

N = int(input())

# a = 1 のとき 2*b^2 <= N なので
c1 = int(math.isqrt(N // 2))

# a = 2 のとき 4*b^2 <= N なので
c2 = int(math.isqrt(N // 4))

print(c1 + c2)
