N = int(input())

# 座標の読み込み
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

count = 0

# 2点の全組み合わせを探索
for i in range(N):
    x1, y1 = points[i]
    for j in range(i + 1, N):
        x2, y2 = points[j]

        dx = x2 - x1
        dy = y2 - y1

        # x座標が一致すると傾きが無限大になるので除外（傾きが定義されない）
        if dx == 0:
            continue

        slope = dy / dx
        # 傾きの範囲が [-1, 1] のときにカウント
        if -1 <= slope <= 1:
            count += 1

print(count)
