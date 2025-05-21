N, T = map(int, input().split())
t = list(map(int, input().split()))

total = 0
# 最後の人までループ
for i in range(N - 1):
    # Tとラグの時間差で短いほう
    total += min(T, t[i + 1] - t[i])
total += T  # 最後の人の分を加算

print(total)
