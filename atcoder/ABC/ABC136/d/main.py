S = input().strip()
N = len(S)

ans = [0] * N

i = 0
while i < N:
    # R の連続部分を伸ばす
    r = i
    while r < N and S[r] == "R":
        r += 1

    # L の連続部分を伸ばす
    l = r
    while l < N and S[l] == "L":
        l += 1

    # 境界の位置
    R_pos = r - 1  # 最後の R
    L_pos = r  # 最初の L

    # R 側 → R_pos へ集まる
    # L 側 → L_pos へ集まる

    # R 連続部分を処理
    for x in range(i, r):
        if (R_pos - x) % 2 == 0:
            ans[R_pos] += 1
        else:
            ans[L_pos] += 1

    # L 連続部分を処理
    for x in range(r, l):
        if (x - L_pos) % 2 == 0:
            ans[L_pos] += 1
        else:
            ans[R_pos] += 1

    # 次のブロックへ
    i = l

print(*ans)
