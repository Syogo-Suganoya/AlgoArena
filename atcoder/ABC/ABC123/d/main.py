import heapq

# 入力
X, Y, Z, K = map(int, input().split())
A = sorted(map(int, input().split()), reverse=True)
B = sorted(map(int, input().split()), reverse=True)
C = sorted(map(int, input().split()), reverse=True)

# A + B のペア和を全部作って降順にソート
AB = []
for a in A:
    for b in B:
        AB.append(a + b)
AB.sort(reverse=True)

# 上位だけで十分（全部必要ではない）
# 大きい順に K 個だけ残すようにカット
AB = AB[:K]

# 優先度付きキューで AB + C を探索
# 要素は (-sum, idx_ab, idx_c) として、最大値から取り出す
pq = []
visited = set()
heapq.heappush(pq, (-(AB[0] + C[0]), 0, 0))
visited.add((0, 0))

ans = []
while len(ans) < K:
    val, i_ab, i_c = heapq.heappop(pq)
    ans.append(-val)

    # 次に進める候補を追加
    if i_ab + 1 < len(AB) and (i_ab + 1, i_c) not in visited:
        heapq.heappush(pq, (-(AB[i_ab + 1] + C[i_c]), i_ab + 1, i_c))
        visited.add((i_ab + 1, i_c))
    if i_c + 1 < len(C) and (i_ab, i_c + 1) not in visited:
        heapq.heappush(pq, (-(AB[i_ab] + C[i_c + 1]), i_ab, i_c + 1))
        visited.add((i_ab, i_c + 1))

# 出力
print("\n".join(map(str, ans)))
