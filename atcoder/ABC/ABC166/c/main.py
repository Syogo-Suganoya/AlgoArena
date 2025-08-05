N, M = map(int, input().split())
A = list(map(int, input().split()))

# 無向グラフの構築
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1  # 0-index に変換
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

# 各頂点をチェック
count = 0
for i in range(N):
    is_good = True
    for neighbor in graph[i]:
        if A[i] <= A[neighbor]:
            is_good = False
            break
    if is_good:
        count += 1

print(count)
