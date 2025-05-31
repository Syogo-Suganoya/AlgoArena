N, D = map(int, input().split())
S = [input() for _ in range(N)]

max_streak = 0  # 最大の連続日数
current_streak = 0  # 現在の連続日数

for day in range(D):
    # 各日(day)における全員のスケジュールを抽出
    today_statuses = [S[person][day] for person in range(N)]

    # set()で全員の状態が 'o' のみかを判定
    if set(today_statuses) == {"o"}:
        current_streak += 1
        max_streak = max(max_streak, current_streak)
    else:
        current_streak = 0  # 途中で 'x' があればリセット

print(max_streak)
