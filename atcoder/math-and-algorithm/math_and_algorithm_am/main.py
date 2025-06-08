import sys

# 再帰の最大深さを引き上げる（デフォルトは1000程度なので、深いグラフ探索でエラーになることを防ぐ）
sys.setrecursionlimit(120000)

# 頂点数 N と 辺数 M の入力
N, M = map(int, input().split())

# 辺情報を格納するリスト（1-indexed）
A = [0] * (M + 1)
B = [0] * (M + 1)
for i in range(1, M + 1):
    A[i], B[i] = map(int, input().split())

# 隣接リストによるグラフの構築
G = [list() for _ in range(N + 1)]
for i in range(1, M + 1):
    G[A[i]].append(B[i])  # A[i] → B[i] の辺を追加
    G[B[i]].append(A[i])  # 無向グラフなので、B[i] → A[i] も追加

# 訪問済みかどうかを記録するリスト
visited = [False] * (N + 1)


# 再帰的に DFS を行う関数
def dfs(pos, G, visited):
    visited[pos] = True  # 現在の頂点を訪問済みにする
    for nex in G[pos]:  # 隣接する頂点を調べる
        if not visited[nex]:  # まだ訪問していなければ、再帰的に DFS
            dfs(nex, G, visited)


# 1 番頂点から探索を開始
dfs(1, G, visited)

# グラフが連結かどうかを判定（すべての頂点が訪問済みであるか）
answer = True
for i in range(1, N + 1):
    if not visited[i]:
        answer = False
        break

# 結果を出力
if answer:
    print("The graph is connected.")
else:
    print("The graph is not connected.")
