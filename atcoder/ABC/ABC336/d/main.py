n = int(input())
a = list(map(int, input().split()))

# 左からの制約を計算
left = [0] * n
left[0] = 1
for i in range(1, n):
    left[i] = min(left[i - 1] + 1, a[i])

# 右からの制約を計算
right = [0] * n
right[-1] = 1
for i in range(n - 2, -1, -1):
    right[i] = min(right[i + 1] + 1, a[i])

# 各位置での最大ピラミッドサイズを求め、全体の最大値を計算
max_size = 0
for i in range(n):
    max_size = max(max_size, min(left[i], right[i]))

print(max_size)
