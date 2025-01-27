from collections import defaultdict


def dfs(current, distance):
    # 現在の地点と距離を記録し、最長距離を更新
    max_distance = distance
    visited[current] = True
    for neighbor, cost in graph[current]:
        if not visited[neighbor]:
            max_distance = max(max_distance, dfs(neighbor, distance + cost))
    visited[current] = False
    return max_distance


# 入力の読み込み
N, M = map(int, input().split())
visited = [False] * (N + 1)

graph = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
result = 0
for start in range(1, N + 1):
    result = max(result, dfs(start, 0))


# 答えの出力
print(result)
