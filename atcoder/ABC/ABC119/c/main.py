from itertools import product

N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]

INF = 10**9
ans = INF

# 各竹を「どこに使うか」割り当てる: 0=捨てる, 1=A, 2=B, 3=C
for pat in product(range(4), repeat=N):
    a, b, c = 0, 0, 0  # それぞれの長さ
    ca, cb, cc = 0, 0, 0  # それぞれ合体に使った本数

    for i in range(N):
        if pat[i] == 1:
            a += L[i]
            ca += 1
        elif pat[i] == 2:
            b += L[i]
            cb += 1
        elif pat[i] == 3:
            c += L[i]
            cc += 1
        # pat[i] == 0 の場合は捨てる

    # どれかに1本も割り当てられなければ不成立
    if ca == 0 or cb == 0 or cc == 0:
        continue

    # コスト計算
    cost = 0
    cost += abs(a - A) + abs(b - B) + abs(c - C)  # 調整コスト
    cost += (ca - 1) * 10 + (cb - 1) * 10 + (cc - 1) * 10  # 合体コスト

    ans = min(ans, cost)

print(ans)
