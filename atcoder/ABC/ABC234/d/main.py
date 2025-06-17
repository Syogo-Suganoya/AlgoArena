import heapq

N, K = map(int, input().split())
P = list(map(int, input().split()))

hq = []
# ステップ①：最初のK個を入れる
for i in range(K):
    heapq.heappush(hq, P[i])
print(hq[0])  # K番目に大きい値

# ステップ②：残りを順に処理
for x in P[K:]:
    heapq.heappush(hq, x)  # 追加
    heapq.heappop(hq)  # 小さい方（K+1番目）を削除
    print(hq[0])  # 現在のK番目に大きい
