from collections import deque

# n: 頂点数, m: 辺の数
n, m = map(int, input().split())

# 隣接リストの作成。各要素は (隣接頂点, XOR値) のタプル
g = [[] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    x, y = x - 1, y - 1  # 0-indexedに変換
    g[x].append((y, z))
    g[y].append((x, z))

# BFS用に訪問済みフラグと頂点の値を管理
visited = [False] * n
val = [-1] * n  # -1は未定義を意味する


def bfs(start):
    """startからBFSで同じ連結成分の頂点を探索し、valを決定する"""
    dq = deque([start])
    visited[start] = True
    comp = [start]  # この連結成分の頂点リスト

    while dq:
        v = dq.popleft()
        for u, w in g[v]:
            if not visited[u]:
                visited[u] = True
                # XORの関係から val[u] を決定
                val[u] = val[v] ^ w
                comp.append(u)
                dq.append(u)
            else:
                # すでに決まっている値と矛盾がある場合は解なし
                if val[u] != val[v] ^ w:
                    print("-1")
                    exit()
    return comp


# 最終的に求める各頂点の答え
ans = [0] * n

# すべての連結成分ごとに処理
for st in range(n):
    if visited[st]:
        continue
    val[st] = 0  # 連結成分の起点の値を0と仮定
    comp = bfs(st)  # BFSで値を決定

    # 各ビットごとに最終値を決定
    for i in range(30):  # 最大30ビットまで（問題の制約に応じて）
        cnt = 0
        # 連結成分内でiビットが1の頂点数を数える
        for j in comp:
            if val[j] & (1 << i):
                cnt += 1
        # 1が少ない場合は1の頂点にビットを立て、0が少ない場合は0の頂点にビットを立てる
        if cnt < len(comp) - cnt:
            for j in comp:
                if val[j] & (1 << i):
                    ans[j] |= 1 << i
        else:
            for j in comp:
                if not (val[j] & (1 << i)):
                    ans[j] |= 1 << i

# 答えの出力
print(*ans)
