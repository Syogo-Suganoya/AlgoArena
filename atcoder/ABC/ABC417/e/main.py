import sys

sys.setrecursionlimit(10**6)

N = 1000  # 頂点数の上限


def dfs(k):
    cand[k] = True
    for to in e[k]:
        if not cand[to] and not used[to]:
            dfs(to)


t = int(input())
for _ in range(t):
    n, m, x, y = map(int, input().split())
    x -= 1
    y -= 1
    e = [[] for _ in range(n)]
    used = [False] * n
    cand = [False] * n

    for _ in range(m):
        u, v = map(int, input().split())
        e[u - 1].append(v - 1)
        e[v - 1].append(u - 1)

    ans = []
    cur = x
    while cur != y:
        ans.append(cur)
        used[cur] = True
        # cand配列をリセット
        for i in range(n):
            cand[i] = False
        # yからの到達可能ノードをDFSでマーキング
        dfs(y)
        nxt = n  # 大きい値で初期化
        for to in e[cur]:
            if cand[to]:
                nxt = min(nxt, to)
        cur = nxt
    ans.append(y)
    print(*[a + 1 for a in ans])
