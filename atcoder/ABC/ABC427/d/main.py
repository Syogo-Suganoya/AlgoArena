T = int(input())
for _ in range(T):
    n, m, k = map(int, input().split())
    s = input().strip()

    # グラフを作成
    G = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append(v)

    # dp[i] = 現在のターンで頂点iで勝てるか (True=Alice勝ち, False=Bob勝ち)
    dp = [c == "A" for c in s]

    for _ in range(k):
        # Bob のターン: 自分のどの選択肢も勝てなければ負け
        ep = [all(dp[j] for j in G[i]) if G[i] else False for i in range(n)]
        dp = ep

        # Alice のターン: どれか一つでも勝てれば勝ち
        ep = [any(dp[j] for j in G[i]) if G[i] else False for i in range(n)]
        dp = ep

    print("Alice" if dp[0] else "Bob")
