from collections import defaultdict

# 入力の読み込み
N = int(input())
# その日に何人ログインしていたか
events = defaultdict(int)

for _ in range(N):
    A, L = map(int, input().split())
    events[A] += 1
    events[A + L] -= 1

# イベントの日付をソート
sorted_days = sorted(events.keys())

# ちょうどK人がログインしていた日数
result = [0] * (N + 1)
current_players = 0
previous_day = 0

for day in sorted_days:
    if current_players > 0:
        result[current_players] += day - previous_day
    current_players += events[day]
    previous_day = day

# 結果の出力
print(" ".join(map(str, result[1:])))
