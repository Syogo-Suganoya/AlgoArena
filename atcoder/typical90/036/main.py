N, Q = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(N)]
queries = [int(input()) - 1 for _ in range(Q)]  # 0-index に直す

# 各点を (u, v) に変換
us = [x + y for x, y in points]
vs = [x - y for x, y in points]

# u, v の最大・最小を前計算
max_u, min_u = max(us), min(us)
max_v, min_v = max(vs), min(vs)

# 各クエリに答える
for qi in queries:
    u, v = us[qi], vs[qi]

    # その点から最も遠い距離は「端点との差」の最大値
    cand = [
        abs(u - max_u),
        abs(u - min_u),
        abs(v - max_v),
        abs(v - min_v),
    ]
    print(max(cand))
