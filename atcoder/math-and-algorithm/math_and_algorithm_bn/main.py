# 区間の数
N = int(input())
intervals = []

# 入力: 開始時間と終了時間
for _ in range(N):
    s, t = map(int, input().split())
    intervals.append((s, t))

# 終了時間でソート
intervals.sort(key=lambda x: x[1])

# 貪欲に選択
count = 0
last_end = 0

for s, t in intervals:
    if s >= last_end:
        count += 1  # 選べる区間
        last_end = t  # 最後に選んだ区間の終了時刻を更新

print(count)
