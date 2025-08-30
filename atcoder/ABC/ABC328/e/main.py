from collections import defaultdict


def solve():
    N, M, K = map(int, input().split())
    edges = []
    for _ in range(M):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v, w))

    # dp[mask] = mask で表される頂点集合の全域木のコストの集合
    dp = defaultdict(set)
    dp[1 << 0] = {0}  # 頂点 0 をスタートとする

    for mask in range(1 << N):
        if mask not in dp:
            continue
        for u, v, w in edges:
            # u が含まれていて v がまだのとき
            if (mask >> u) & 1 and not (mask >> v) & 1:
                next_mask = mask | (1 << v)
                for cost in dp[mask]:
                    dp[next_mask].add((cost + w) % K)
            # v が含まれていて u がまだのとき
            elif (mask >> v) & 1 and not (mask >> u) & 1:
                next_mask = mask | (1 << u)
                for cost in dp[mask]:
                    dp[next_mask].add((cost + w) % K)

    # 全頂点を含む mask の中で最小の mod K 値
    full_mask = (1 << N) - 1
    print(min(dp[full_mask]))


solve()
