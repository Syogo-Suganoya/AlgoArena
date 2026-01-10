import heapq

N, K, X = map(int, input().split())
A = list(map(int, input().split()))

# 1. スコアを降順（大きい順）にソート
A.sort(reverse=True)

# 2. 最大スコア（すべて A[0] を選んだ場合）
max_score = K * A[0]

# 最初の最大値を出力
print(max_score)
if X == 1:
    exit()

# 3. 差分コスト D の計算
# D[i] は A[0] を A[i] に入れ替えた時に減るスコア量
D = [A[0] - A[i] for i in range(N)]

# 4. 優先度付きキュー (最小ヒープ)
# (現在の合計コスト, 注目している A のインデックス i, 入れ替えた個数)
# 最初は「A[0] を 1 つ A[1] に変えた」状態を入れる
hq = [(D[1], 1, 1)]

count_found = 1  # すでに出力した件数

while hq and count_found < X:
    cost, i, count = heapq.heappop(hq)

    # スコアを出力（最大値 - 減少分）
    print(max_score - cost)
    count_found += 1

    # 次の候補（状態）を生成してヒープに追加
    # ルール1: 同じ種類 i のアイテムをさらにもう一つ入れ替える
    if count < K:
        heapq.heappush(hq, (cost + D[i], i, count + 1))

    # ルール2: 最後に変えた種類 i のうち 1 つを、さらに 1 つ下のランク i+1 に変える
    if i + 1 < N:
        # 「i を 1 つ減らして i+1 を 1 つ増やす」操作
        new_cost = cost - D[i] + D[i + 1]
        heapq.heappush(hq, (new_cost, i + 1, count))
