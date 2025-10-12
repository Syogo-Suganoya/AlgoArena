T = int(input())
for _ in range(T):
    n, m, k = map(int, input().split())
    s = input().strip()

    # グラフ作成
    G = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append(v)

    # dp[i] = 現在のターンで頂点iで勝てるか
    dp = [c == "A" for c in s]

    for turn in range(2 * k):
        if turn % 2 == 0:  # Bobのターン
            dp = [all(dp[j] for j in G[i]) if G[i] else False for i in range(n)]
        else:  # Aliceのターン
            dp = [any(dp[j] for j in G[i]) if G[i] else False for i in range(n)]

    print("Alice" if dp[0] else "Bob")
