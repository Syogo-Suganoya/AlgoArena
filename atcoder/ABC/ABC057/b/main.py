N, M = map(int, input().split())

# 生徒の座標リスト
s = [tuple(map(int, input().split())) for _ in range(N)]

# チェックポイントの座標リスト
c = [tuple(map(int, input().split())) for _ in range(M)]

for si in s:
    min_dist = float("inf")
    min_idx = -1
    for j, cj in enumerate(c):
        # マンハッタン距離を計算
        dist = abs(si[0] - cj[0]) + abs(si[1] - cj[1])
        if dist < min_dist:
            min_dist = dist
            min_idx = j + 1  # 出力は1-indexed
    print(min_idx)
