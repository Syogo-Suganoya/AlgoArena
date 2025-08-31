import heapq

N = int(input())
TD = [tuple(map(int, input().split())) for _ in range(N)]

# 商品を (T, T+D) の形に変換
tasks = [(t, t + d) for t, d in TD]
# 開始時刻でソート
tasks.sort()

res = 0
pq = []  # 優先度付きキュー（終了時刻を入れる）
t = 0
i = 0

while i < N or pq:
    # 印字可能な商品をキューに追加
    while i < N and tasks[i][0] <= t:
        heapq.heappush(pq, tasks[i][1])  # 終了時刻をpush
        i += 1

    # 印字できない（すでに範囲外に出た）商品を削除
    while pq and pq[0] < t:
        heapq.heappop(pq)

    if pq:
        # 最も早く終わる商品を選んで印字
        heapq.heappop(pq)
        res += 1
        t += 1  # クールタイム1
    else:
        # 候補がない場合 → 次の商品が出てくる時刻までジャンプ
        if i < N:
            t = tasks[i][0]
        else:
            break

print(res)
