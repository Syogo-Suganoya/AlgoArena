import heapq

N, K = map(int, input().split())
A = list(map(int, input().split()))

# 最小ヒープの初期化
min_heap = [0]
# 訪問済みの合計金額を管理する集合
visited = set([0])

# K 回目の合計金額を求める
for _ in range(K):
    # 最小の合計金額を取り出す
    current = heapq.heappop(min_heap)
    # 各たこ焼きの価格を加えた新しい合計金額を生成
    for price in A:
        new_sum = current + price
        if new_sum not in visited:
            visited.add(new_sum)
            heapq.heappush(min_heap, new_sum)

# K 回目の合計金額を返す
print(heapq.heappop(min_heap))
