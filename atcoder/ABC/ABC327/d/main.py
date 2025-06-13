from collections import defaultdict, deque

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# グラフ構築
graph = defaultdict(list)
for a, b in zip(A, B):
    graph[a].append(b)
    graph[b].append(a)

# 二部グラフ判定用の色管理（0:未訪問, 1, -1）
color = dict()


def is_bipartite(start):
    queue = deque([start])
    color[start] = 1
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in color:
                color[neighbor] = -color[node]
                queue.append(neighbor)
            elif color[neighbor] == color[node]:
                return False
    return True


# 全ノードを確認（非連結な成分があってもOKなように）
for v in set(A + B):
    if v not in color:
        if not is_bipartite(v):
            print("No")
            break
else:
    print("Yes")
