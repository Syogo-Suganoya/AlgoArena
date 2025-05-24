# N: 食材の数, M: 料理の数
N, M = map(int, input().split())

# 各料理が使う食材の情報を格納するリスト
# 各要素は、ある料理に必要な食材の番号の集合
A = []
for _ in range(M):
    KA = list(map(int, input().split()))
    A.append(set(KA[1:]))

# 食材が克服される順番 (1-indexed)
B = list(map(int, input().split()))

# 食材番号 -> 何日目に克服されるかの辞書
day_of_cure = dict()
for i, food in enumerate(B):
    day_of_cure[food] = i  # 0-indexed の日数で管理する

# 各料理が「すべての食材が克服された日」を求める
# 料理に含まれる食材の中で、最も遅く克服される食材の日
# -> その日以降、料理が食べられるようになる
count = [0] * N  # 各日ごとに新たに食べられるようになる料理の数
for ingredients in A:
    latest_day = 0
    for food in ingredients:
        # その食材が克服される日を取得
        latest_day = max(latest_day, day_of_cure[food])
    # その日以降に食べられる料理としてカウント
    count[latest_day] += 1

# 各日までに食べられる料理の累積数を出力
res = 0
for c in count:
    res += c
    print(res)
