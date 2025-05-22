D, N = map(int, input().split())

# 各日の労働時間の初期上限を24時間に設定（D日分）
max_hours = [24] * D

# N個の制約を順に適用していく
for _ in range(N):
    L, R, H = map(int, input().split())

    # 制約：L日目からR日目まで、各日最大H時間しか働けない
    for day in range(L - 1, R):  # Pythonの配列は0-indexなので、L-1からR-1まで
        # 各日の上限を、現在の上限とHの小さい方に更新
        max_hours[day] = min(max_hours[day], H)

# 制約後の各日の労働上限をすべて足し合わせる
total_work_time = sum(max_hours)

print(total_work_time)
