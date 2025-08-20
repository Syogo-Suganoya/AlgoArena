import heapq

# 入力
h, w, y = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

# 各マスの水没までの年数（初期値 y+1）
dist = [[y + 1] * w for _ in range(h)]

# 優先度付きキュー（距離, i, j）※heapqは最小ヒープなので負の値で疑似最大ヒープ
q = []


def upd(i, j, v):
    if dist[i][j] > v:
        dist[i][j] = v
        heapq.heappush(q, (-dist[i][j], i, j))


# 外周を初期化
for j in range(w):
    upd(0, j, a[0][j])
    upd(h - 1, j, a[h - 1][j])
for i in range(h):
    upd(i, 0, a[i][0])
    upd(i, w - 1, a[i][w - 1])

# ダイクストラ風 BFS
while q:
    d, i, j = heapq.heappop(q)
    d = -d
    if dist[i][j] != d:
        continue
    for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if 0 <= ni < h and 0 <= nj < w:
            upd(ni, nj, max(dist[i][j], a[ni][nj]))

# 結果集計
ans = [0] * (y + 2)
for i in range(h):
    for j in range(w):
        ans[dist[i][j] - 1] += 1

for i in range(y, -1, -1):
    ans[i] += ans[i + 1]

for i in range(1, y + 1):
    print(ans[i])
