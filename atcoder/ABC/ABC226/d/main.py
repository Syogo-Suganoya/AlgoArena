import math

N = int(input())  # 都市の数を受け取る
points = [tuple(map(int, input().split())) for _ in range(N)]  # 各都市の座標を取得

directions = set()  # 移動ベクトルの向きを一意に管理する集合

# すべての都市のペアに対して調べる
for i in range(N):
    for j in range(N):
        if i == j:
            continue  # 同じ都市同士はスキップ

        # 都市iから都市jへのベクトルを計算
        dx = points[j][0] - points[i][0]
        dy = points[j][1] - points[i][1]

        # dx, dy の最大公約数を使ってベクトルを正規化
        g = math.gcd(dx, dy)
        dx //= g
        dy //= g

        # 正規化したベクトルを集合に追加（重複が除かれる）
        directions.add((dx, dy))

# 集合にある方向ベクトルの数が、必要な移動方法の最小数
print(len(directions))
