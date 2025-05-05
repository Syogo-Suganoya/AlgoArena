import math

N, S, M, L = map(int, input().split())
ans = float("inf")


for i in range(N // 6 + 2):
    for j in range(N // 8 + 2):
        rest = N - i * 6 - j * 8
        if rest <= 0:
            k = 0
        else:
            k = math.ceil(rest / 12)
        tmp = i * S + j * M + k * L
        ans = min(ans, tmp)

print(ans)
