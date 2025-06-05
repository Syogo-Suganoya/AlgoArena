N = int(input())
events = []

# 各プレイヤーのログイン開始と終了をイベントとして記録
for _ in range(N):
    A, B = map(int, input().split())
    events.append((A, 1))  # ログイン開始：+1
    events.append((A + B, -1))  # ログイン終了：-1

# イベントを日付順にソート
events.sort()

ans = [0] * (N + 1)
current_day = events[0][0]
current_count = 0

for day, change in events:
    if day != current_day:
        duration = day - current_day
        ans[current_count] += duration
        current_day = day
    current_count += change

# 結果を出力（1人以上のログイン人数の日数）
print(*ans[1:])
