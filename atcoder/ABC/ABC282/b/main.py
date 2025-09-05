from itertools import combinations

N, M = map(int, input().split())
S = [list(input().strip()) for _ in range(N)]

# 各行を bit 化
rows = []
for row in S:
    bit = 0
    for j, c in enumerate(row):
        if c == "o":  # "o" が 1 を表すと仮定
            bit |= 1 << j
    rows.append(bit)

FULL = (1 << M) - 1

ans = 0
for i, j in combinations(range(N), 2):
    if (rows[i] | rows[j]) == FULL:  # 2行で全ての列をカバー
        ans += 1

print(ans)
