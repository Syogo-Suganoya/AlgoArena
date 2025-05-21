X = int(input())
max_time = 1000  # 十分大きな時刻まで探索
offset = max_time * (max_time + 1) // 2  # 座標のオフセット
size = offset * 2 + 1  # 座標の範囲

dp = [set() for _ in range(max_time + 2)]
dp[0].add(0)

for i in range(max_time):
    for pos in dp[i]:
        dp[i + 1].add(pos + i + 1)
        dp[i + 1].add(pos - i + 1)
        dp[i + 1].add(pos)

    if X in dp[i + 1]:
        print(i + 1)
        break
