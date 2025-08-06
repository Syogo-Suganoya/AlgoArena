from itertools import combinations_with_replacement

N, M, Q = map(int, input().split())
conds = [tuple(map(int, input().split())) for _ in range(Q)]

ans = 0
# 非減少列の全列挙
for A in combinations_with_replacement(range(1, M + 1), N):
    score = 0
    for a, b, c, d in conds:
        if A[b - 1] - A[a - 1] == c:
            score += d
    ans = max(ans, score)

print(ans)
