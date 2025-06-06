N = int(input())
A = list(map(int, input().split()))

max_count = 0
best_x = 0

for x in range(2, 1001):
    count = sum(a % x == 0 for a in A)  # x で割り切れる数をカウント
    if count > max_count:
        max_count = count
        best_x = x

print(best_x)
