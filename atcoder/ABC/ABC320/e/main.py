import heapq

N, M = map(int, input().split())

events = []
for _ in range(M):
    T, W, S = map(int, input().split())
    # 種類 1 = そうめん, 0 = 人が戻る（戻る方を優先）
    heapq.heappush(events, (T, 1, (W, S)))

ans = [0] * N
line = list(range(N))  # 最初は全員が並んでいる
heapq.heapify(line)  # 若番優先にする

while events:
    T, typ, data = heapq.heappop(events)

    if typ == 1:  # そうめん流れる
        W, S = data
        if line:  # 誰か並んでいれば
            person = heapq.heappop(line)  # 若番を取り出す
            ans[person] += W
            # S秒後に戻る（戻りは typ=0）
            heapq.heappush(events, (T + S, 0, person))

    else:  # 人が列に戻る
        person = data
        heapq.heappush(line, person)

# 出力
print("\n".join(map(str, ans)))
