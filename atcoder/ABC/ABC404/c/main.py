from collections import defaultdict

N, M = map(int, input().split())
if N != M:
    print("No")
    exit()

graph = defaultdict(list)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

# 適当な頂点から順にたどる
start = 1
current = start
prev = -1
count = 0

while True:
    count += 1
    # 次に進む頂点を決定（前の頂点には戻らない）
    for neighbor in graph[current]:
        if neighbor != prev:
            next_node = neighbor
            break
    prev, current = current, next_node
    if current == start:  # 元に戻った
        break
    if count > N:  # 無限ループ防止
        print("No")
        exit()

# 長さがNなら完全サイクル
if count == N:
    print("Yes")
else:
    print("No")
