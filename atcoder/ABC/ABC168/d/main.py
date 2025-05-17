from collections import deque

# 入力の読み込み
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

# グラフの構築
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 各部屋への最短経路上の直前の部屋を記録するリスト
prev = [-1] * (N + 1)
prev[1] = 0  # 部屋1は始点なので0とする

# 幅優先探索（BFS）
queue = deque([1])
while queue:
    current = queue.popleft()
    for neighbor in graph[current]:
        if prev[neighbor] == -1:
            prev[neighbor] = current
            queue.append(neighbor)

# 結果の出力
print("Yes")
for i in range(2, N + 1):
    print(prev[i])
