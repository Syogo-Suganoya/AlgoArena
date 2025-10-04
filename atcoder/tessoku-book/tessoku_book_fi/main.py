N, K = map(int, input().split())
A = list(map(int, input().split()))

# 二分探索する範囲（閾値 T）
low, high = 0.0, max(A)  # スコアは最大でA[i]

for _ in range(60):  # 精度十分
    mid = (low + high) / 2
    # mid以上を取れる議席数を数える
    cnt = 0
    for a in A:
        cnt += int(a // mid)
    if cnt >= K:
        low = mid
    else:
        high = mid

# 閾値T = lowで確定
T = low
seats = [0] * N
remain = K

for i in range(N):
    seats[i] = int(A[i] // T)
    remain -= seats[i]

# 残りの議席をスコアの高い順に調整
scores = []
for i in range(N):
    next_val = A[i] / (seats[i] + 1)
    scores.append((next_val, i))

scores.sort(reverse=True)
for _, i in scores[:remain]:
    seats[i] += 1

print(*seats)
