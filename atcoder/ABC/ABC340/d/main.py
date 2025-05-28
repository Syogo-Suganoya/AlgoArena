import heapq

N = int(input())
A = []
B = []
C = []

for _ in range(N - 1):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)

# 各ステージの最短到達時間を初期化
dist = [float("inf")] * N
dist[0] = 0

# 優先度付きキューを初期化
hq = [(0, 0)]  # (現在の時間, 現在のステージ)

while hq:
    time, stage = heapq.heappop(hq)
    if dist[stage] < time:
        continue
    if stage < N - 1:
        # ステージ i をクリアして i+1 に進む
        if dist[stage + 1] > time + A[stage]:
            dist[stage + 1] = time + A[stage]
            heapq.heappush(hq, (dist[stage + 1], stage + 1))
        # ステージ i から C_i にワープする
        if dist[C[stage] - 1] > time + B[stage]:
            dist[C[stage] - 1] = time + B[stage]
            heapq.heappush(hq, (dist[C[stage] - 1], C[stage] - 1))

print(dist[N - 1])
