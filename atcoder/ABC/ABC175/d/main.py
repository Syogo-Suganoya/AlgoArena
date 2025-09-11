n, k = map(int, input().split())
P = list(map(lambda x: int(x) - 1, input().split()))  # 0-index に変換
C = list(map(int, input().split()))

ans = -(10**18)  # 最小値で初期化

for start in range(n):
    # ---- サイクルの合計値を調べる ----
    cycle = []
    pos = start
    score = 0
    while True:
        pos = P[pos]
        cycle.append(C[pos])
        score += C[pos]
        if pos == start:
            break

    m = len(cycle)  # サイクルの長さ

    # ---- k 歩以内に取れる最大値を求める ----
    total = 0
    for i in range(m):
        total += cycle[i]
        steps = i + 1  # ここまででの歩数

        if steps > k:
            break

        # サイクルを何周できるか
        cnt = (k - steps) // m
        # サイクルの合計が正なら何周かして得点を増やせる
        if score > 0:
            candidate = total + score * cnt
        else:
            candidate = total

        ans = max(ans, candidate)

print(ans)
