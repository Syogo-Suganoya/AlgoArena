from collections import Counter

N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]

ans = 0

# 2^N通りの部分集合を全探索
for bit in range(1 << N):
    cnt = Counter()

    # ビットが立っているS[i]をカウントに加算
    for i in range(N):
        if bit & (1 << i):
            cnt.update(S[i])

    # 各文字の出現回数がちょうど M のものを数える
    res = sum(1 for v in cnt.values() if v == M)
    ans = max(ans, res)

print(ans)
