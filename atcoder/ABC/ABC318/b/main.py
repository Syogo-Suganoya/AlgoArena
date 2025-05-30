N = int(input())

SIZE = 101
imos = [[0] * SIZE for _ in range(SIZE)]

for _ in range(N):
    A, B, C, D = map(int, input().split())
    # 左下を+1
    imos[A][C] += 1
    # 右上を+1
    imos[B][D] += 1
    # 右下
    imos[B][C] -= 1
    # 左上
    imos[A][D] -= 1

# 横方向の累積和
for i in range(SIZE):
    for j in range(1, SIZE):
        imos[i][j] += imos[i][j - 1]

# 縦方向の累積和
for j in range(SIZE):
    for i in range(1, SIZE):
        imos[i][j] += imos[i - 1][j]

# 1以上のマスのカウント
res = 0
for i in range(SIZE):
    for j in range(SIZE):
        if imos[i][j] > 0:
            res += 1

print(res)
