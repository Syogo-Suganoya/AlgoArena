import math

N = int(input())
A = [int(input()) for _ in range(N)]

res = A[0]
for i in range(1, N):
    res = math.lcm(res, A[i])

print(res)
