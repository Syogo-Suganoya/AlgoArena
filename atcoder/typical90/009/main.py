from math import atan2, degrees

n = int(input())
# 点の座標を読み込む
xy = [[int(x) for x in input().split()] for _ in range(n)]
ans = 0
eps = 1e-10  # 浮動小数誤差対策用の微小値

# 各点を「中心」として考える
for i in range(n):
    x, y = xy[i]
    lists = []

    # 他の点から中心点へのベクトルの角度を計算
    for k in range(n):
        if k == i:
            continue
        # atan2(dy, dx) は [-180°, 180°] の角度を返す
        theta = degrees(atan2(xy[k][1] - y, xy[k][0] - x))
        # マイナスの値を補正して [0°, 360°) に直す
        if theta < 0:
            theta += 360
        lists.append(theta)

    # 昇順に並べ替える
    lists.sort()
    m = len(lists)
    # 360°を足した配列をつなげることで、円周を直線化して扱えるようにする
    lists += [x + 360 for x in lists]

    # two-pointer 法で最大角度を求める
    n_idx = 0
    for idx in range(m):
        # lists[idx] を基準にして、180°以内で収まる一番遠い点を探す
        while n_idx < idx + m and lists[n_idx] - lists[idx] <= 180 + eps:
            # 角度の差を最大値候補に更新
            ans = max(ans, lists[n_idx] - lists[idx])
            n_idx += 1

# 最終的な最大角度を出力
print(ans)
