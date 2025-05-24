# 入力：N は円周上の点の数、M は与えられる直線の本数
N, M = map(int, input().split())

# 各方向ごとの直線の本数を格納するリスト（方向は (A + B) % N で一意に定義される）
direction_counts = [0] * N

# M 本の直線情報を読み込む
for _ in range(M):
    A, B = map(int, input().split())
    # 各直線の方向を求める
    direction = (A + B) % N
    # 同じ方向の直線をカウント
    direction_counts[direction] += 1

# まずは全ての直線から 2 本を選ぶ組み合わせ（＝交差の可能性がある全てのペア）
total_intersections = M * (M - 1) // 2

# 同じ方向にある直線の組み合わせ（＝交差しない）を引いていく
for count in direction_counts:
    # 同じ方向の中から2本を選ぶ → これは交差しない
    total_intersections -= count * (count - 1) // 2

# 答えを出力：交差する直線のペア数
print(total_intersections)
