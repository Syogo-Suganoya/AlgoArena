N, M = map(int, input().split())

count = 0
limit = M * M  # 距離比較は二乗で行う

for _ in range(N):
    X, Y = map(int, input().split())

    # 原点からの距離の二乗
    dist2 = X * X + Y * Y

    # 半径M以内ならカウント
    if dist2 <= limit:
        count += 1

print(count)
