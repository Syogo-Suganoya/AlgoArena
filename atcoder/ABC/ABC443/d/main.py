import heapq

T = int(input())

for _ in range(T):
    n = int(input())
    r = list(map(int, input().split()))

    # 最終的な値を入れる配列（最初は元と同じ）
    a = r[:]

    # 優先度付きキュー（小さい順に取り出される）
    # (値, インデックス)
    pq = []
    for i in range(n):
        heapq.heappush(pq, (a[i], i))

    while pq:
        ai, i = heapq.heappop(pq)

        # 古い情報なら無視
        if a[i] != ai:
            continue

        # 左を見る
        if i != 0 and a[i - 1] > a[i] + 1:
            a[i - 1] = a[i] + 1
            heapq.heappush(pq, (a[i - 1], i - 1))

        # 右を見る
        if i != n - 1 and a[i + 1] > a[i] + 1:
            a[i + 1] = a[i] + 1
            heapq.heappush(pq, (a[i + 1], i + 1))

    # どれだけ削ったか
    ans = 0
    for i in range(n):
        ans += r[i] - a[i]

    print(ans)
