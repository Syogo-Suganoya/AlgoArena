from collections import deque

N, M = map(int, input().split())

# 各色ごとの処理キュー
que = deque()

# 各筒のボールをキューで保持
A = []
for _ in range(M):
    k = int(input())
    balls = deque(int(x) - 1 for x in input().split())  # 0-indexed
    A.append(balls)

# 各色のボールが入っている筒の番号を記録
mem = [[] for _ in range(N)]
for i, q in enumerate(A):
    if q:
        mem[q[0]].append(i)

# 初期状態で同じ色が2つ揃っている色を que に追加
for i in range(N):
    if len(mem[i]) == 2:
        que.append(i)

# メイン処理
while que:
    now = que.popleft()
    for p in mem[now]:
        A[p].popleft()  # 一番上のボールを取り出す
        if A[p]:
            mem[A[p][0]].append(p)
            if len(mem[A[p][0]]) == 2:
                que.append(A[p][0])

# 結果判定
if all(len(q) == 0 for q in A):
    print("Yes")
else:
    print("No")
