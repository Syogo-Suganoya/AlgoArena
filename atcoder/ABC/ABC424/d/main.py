N = int(input())
for _ in range(N):
    H, W = map(int, input().split())
    maze = [input().strip() for _ in range(H)]

    # 各行をビット表現に
    orig = []
    for r in maze:
        mask = 0
        for j, c in enumerate(r):
            if c == "#":
                mask |= 1 << j
        orig.append(mask)

    # 各行に対して、塗り替えコストを前計算
    cost = [[0] * (1 << W) for _ in range(H)]
    for i in range(H):
        for mask in range(1 << W):
            diff = 0
            for j in range(W):
                bit = (mask >> j) & 1
                origbit = (orig[i] >> j) & 1
                if bit != origbit:
                    diff += 1
            cost[i][mask] = diff

    INF = 10**9
    dp = [[INF] * (1 << W) for _ in range(H)]
    for mask in range(1 << W):
        dp[0][mask] = cost[0][mask]

    # 遷移
    for i in range(1, H):
        for prev in range(1 << W):
            if dp[i - 1][prev] == INF:
                continue
            for cur in range(1 << W):
                # 2x2 が全部黒になるかチェック
                bad = False
                for j in range(W - 1):
                    if (
                        ((prev >> j) & 1)
                        and ((prev >> (j + 1)) & 1)
                        and ((cur >> j) & 1)
                        and ((cur >> (j + 1)) & 1)
                    ):
                        bad = True
                        break
                if bad:
                    continue
                dp[i][cur] = min(dp[i][cur], dp[i - 1][prev] + cost[i][cur])

    ans = min(dp[H - 1])
    print(ans)
