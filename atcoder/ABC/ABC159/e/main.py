H, W, K = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(H)]

ans = 10**9

# 横方向の切り方を全探索（ビット全探索）
for mask in range(1 << (H - 1)):
    # 横の分割数
    g = bin(mask).count("1") + 1

    # 各グループごとのカウントを格納
    cnt = [0] * g
    cuts = g - 1  # 横切り回数（グループ数-1）

    ok = True
    j = 0
    while j < W:
        # 各列の白の数をグループごとにカウント
        tmp = [0] * g
        cur = 0
        for i in range(H):
            tmp[cur] += grid[i][j]
            if (mask >> i) & 1:  # i 行目の下で切る
                cur += 1

        # 今の列を加えても K を超えないか判定
        for k in range(g):
            if tmp[k] > K:
                ok = False
                break
        if not ok:
            break

        if all(cnt[k] + tmp[k] <= K for k in range(g)):
            # まだ K を超えない → この列を追加
            for k in range(g):
                cnt[k] += tmp[k]
            j += 1
        else:
            # 超えてしまう → 縦に切る
            cuts += 1
            cnt = tmp[:]
            j += 1

    if ok:
        ans = min(ans, cuts)

print(ans)
