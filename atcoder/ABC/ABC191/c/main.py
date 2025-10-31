H, W = map(int, input().split())
S = [input().strip() for _ in range(H)]

ans = 0
for i in range(H - 1):
    for j in range(W - 1):
        # 2×2 ブロックを調べる
        cnt = 0
        if S[i][j] == "#":
            cnt += 1
        if S[i + 1][j] == "#":
            cnt += 1
        if S[i][j + 1] == "#":
            cnt += 1
        if S[i + 1][j + 1] == "#":
            cnt += 1

        # 黒マスが 1 個または 3 個なら角をカウント
        if cnt == 1 or cnt == 3:
            ans += 1

print(ans)
