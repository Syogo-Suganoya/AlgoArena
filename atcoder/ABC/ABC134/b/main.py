import math

N, M = map(int, input().split())
print(math.ceil(N / (M * 2 + 1)))
