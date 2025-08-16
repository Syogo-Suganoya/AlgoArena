import math

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

count = 0
for i in range(N):
    for j in range(i + 1, N):
        # 距離の二乗を計算
        dist2 = 0
        for k in range(M):
            diff = A[i][k] - A[j][k]
            dist2 += diff * diff

        # 完全平方数チェック
        if int(math.isqrt(dist2)) ** 2 == dist2:
            count += 1

print(count)
