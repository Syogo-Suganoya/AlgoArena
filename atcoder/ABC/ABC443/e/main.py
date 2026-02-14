t = int(input())
for _ in range(t):
    n, c = map(int, input().split())
    c -= 1  # 0-index にする

    s = []
    low = [-1] * n

    # 入力と low の計算
    for i in range(n):
        row = input().strip()
        s.append(row)
        for j in range(n):
            if row[j] == "#":
                low[j] = i

    # dp 配列
    dp = [[0] * n for _ in range(n)]

    # 最下段は開始列 c だけ 1
    for i in range(n):
        dp[i][c] = 1

    # 下から上へ
    for i in range(n - 2, -1, -1):
        for j in range(n):
            if dp[i][j] > 0:
                continue

            ok = False

            # 真下
            if dp[i + 1][j] > 0:
                ok = True
            # 左下
            if j > 0 and dp[i + 1][j - 1] > 0:
                ok = True
            # 右下
            if j + 1 < n and dp[i + 1][j + 1] > 0:
                ok = True

            if ok:
                if s[i][j] == ".":
                    dp[i][j] = 1
                else:
                    if low[j] == i:
                        for k in range(i + 1):
                            dp[k][j] = 1

    print("".join(map(str, dp[0])))
