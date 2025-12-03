from collections import defaultdict

N, C = map(int, input().split())

# 各日における「料金変動」を記録する辞書
# day_change[day] += 金額 という形式
day_change = defaultdict(int)

for _ in range(N):
    a, b, c = map(int, input().split())
    day_change[a] += c  # 課金開始
    day_change[b + 1] -= c  # 課金終了翌日に引く

# 日付が変わるポイントを昇順に取得
days = sorted(day_change.keys())

prev_day = 0
current_cost = 0
total = 0

for day in days:
    if prev_day > 0:
        # 前回の区間の長さ
        length = day - prev_day
        # その区間の1日あたりの課金額（上限 C）
        total += min(current_cost, C) * length

    # この日に料金が変動する
    current_cost += day_change[day]
    prev_day = day

print(total)
