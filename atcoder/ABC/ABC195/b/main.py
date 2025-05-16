A, B, W = map(int, input().split())
W *= 1000  # 重さをkgからgに変換（計算しやすくする）

min_cnt = float("inf")  # 最小個数を求めるために初期値は∞
max_cnt = 0  # 最大個数の初期値は0

# オレンジの個数を全探索（1個〜十分大きい数まで）
for n in range(1, 10**6 + 1):
    min_w = A * n  # 1個Aグラムの場合の最小総重量
    max_w = B * n  # 1個Bグラムの場合の最大総重量
    # この個数nで、Wグラムにできるか？
    if min_w <= W <= max_w:
        min_cnt = min(min_cnt, n)
        max_cnt = max(max_cnt, n)

# 結果出力
if min_cnt == float("inf"):
    print("UNSATISFIABLE")  # どんな個数でもWグラムにできなかった
else:
    print(min_cnt, max_cnt)
