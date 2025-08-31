Rt, Ct, Ra, Ca = map(int, input().split())
N, M, L = map(int, input().split())

# 方向ベクトル
dmap = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

taka_moves = []
for _ in range(M):
    s, a = input().split()
    taka_moves.append((dmap[s], int(a)))

aoki_moves = []
for _ in range(L):
    t, b = input().split()
    aoki_moves.append((dmap[t], int(b)))

ans = 0
i = j = 0
rt, ct = Rt, Ct
ra, ca = Ra, Ca

while i < M and j < L:
    (dRt, dCt), a = taka_moves[i]
    (dRa, dCa), b = aoki_moves[j]
    step = min(a, b)

    if (dRt, dCt) == (dRa, dCa):
        # 同じ方向
        if (rt, ct) == (ra, ca):
            ans += step
    else:
        # 距離チェック
        d = abs(rt - ra) + abs(ct - ca)
        if d % 2 == 0:
            half = d // 2
            if 0 < half <= step:
                # half 歩後に一致するか
                if (
                    rt + dRt * half == ra + dRa * half
                    and ct + dCt * half == ca + dCa * half
                ):
                    ans += 1

    # 双方の位置を更新
    rt += dRt * step
    ct += dCt * step
    ra += dRa * step
    ca += dCa * step

    taka_moves[i] = ((dRt, dCt), a - step)
    aoki_moves[j] = ((dRa, dCa), b - step)
    if taka_moves[i][1] == 0:
        i += 1
    if aoki_moves[j][1] == 0:
        j += 1

print(ans)
