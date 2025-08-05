N, M, X = map(int, input().split())
CA = [list(map(int, input().split())) for _ in range(N)]

INF = float("inf")
res = INF

# 全ての本の選び方（2^N通り）をビットで表現
for bit in range(1, 1 << N):  # 空集合は除く
    cost = 0
    skills = [0] * M  # 各スキルの合計値

    for i in range(N):
        if bit & (1 << i):  # 本iを選んだ場合
            cost += CA[i][0]
            for j in range(M):
                skills[j] += CA[i][j + 1]

    # すべてのスキルがX以上であれば更新
    if all(s >= X for s in skills):
        res = min(res, cost)

print(res if res != INF else -1)
