N, X = map(int, input().split())
A = []
B = []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

INF = 1 << 60
dp = [INF] * (N + 1)
dp[0] = 0

# dp[i]: ステージiまでで、i回分の初回クリアにかかる最小時間
for i in range(1, N + 1):
    dp[i] = dp[i - 1] + A[i - 1] + B[i - 1]

res = INF
for i in range(1, min(N, X) + 1):
    rest = X - i
    res = min(res, dp[i] + rest * B[i - 1])

print(res)


def another():
    """決め打ち全探索"""
    N, X = map(int, input().split())
    A = []
    B = []

    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    min_time = float("inf")
    total_time = 0

    for i in range(min(N, X)):
        total_time += A[i] + B[i]
        remaining = X - (i + 1)
        current_time = total_time + remaining * B[i]
        min_time = min(min_time, current_time)

    print(min_time)
