from collections import deque

Q = int(input())
now = 0  # 現在の時間
l = deque()  # クエリ1で記録される「木材が積まれた時刻」

for _ in range(Q):
    query = list(map(int, input().split()))
    t = query[0]

    if t == 1:
        # 木材を追加：現在時刻を記録
        l.append(now)

    elif t == 2:
        # 時刻を進める
        T = query[1]
        now += T

    elif t == 3:
        # 高さH分だけ燃やす
        H = query[1]
        cnt = 0
        # now - H 未満の時刻の木材を燃やす
        while l and l[0] <= now - H:
            l.popleft()
            cnt += 1
        print(cnt)
