N, K = map(int, input().split())
h = sorted(int(input()) for _ in range(N))

min_diff = float("inf")
# 最低の木を全探索
for i in range(N - K + 1):
    diff = h[i + K - 1] - h[i]
    min_diff = min(min_diff, diff)

print(min_diff)
