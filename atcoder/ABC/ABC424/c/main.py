from collections import deque

N = int(input())
G = [set() for _ in range(N + 1)]

# 入力から隣接リストを作成（重複を削除するため set を使用）
for i in range(1, N + 1):
    a, b = map(int, input().split())
    G[a].add(i)
    G[b].add(i)

visited = [False] * (N + 1)
visited[0] = True

# BFSで到達可能なノードを探索
queue = deque([0])
while queue:
    v = queue.popleft()
    for vv in G[v]:
        if not visited[vv]:
            visited[vv] = True
            queue.append(vv)

# 0を除いた訪問済みノードの個数を出力
print(sum(visited) - 1)
