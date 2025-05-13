N, M = map(int, input().split())

graph = [[] for _ in range(N)]  # 頂点数Nの隣接リスト

# M本の無向辺を読み取る
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1  # 0-indexed に調整
    B -= 1
    graph[A].append(B)
    graph[B].append(A)

res = 0

# 三角形のカウント（重複を避けるため a < b < c に限定）
for a in range(N):
    for b in graph[a]:
        if b <= a:
            continue  # 重複カウントを避ける
        for c in graph[b]:
            if c <= b:
                continue  # 同様に重複を避ける
            if a in graph[c]:  # a - b - c - a が成り立つなら三角形
                res += 1

print(res)
