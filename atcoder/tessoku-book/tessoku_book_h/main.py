H, W = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(H)]

# 2D累積和（1-indexed）
S = [[0] * (W + 1) for _ in range(H + 1)]
for y in range(1, H + 1):
    for x in range(1, W + 1):
        # 上の長方形+左の長方形-上と左で二重に数えた部分+今いるマス maze[y-1][x-1]
        S[y][x] = S[y - 1][x] + S[y][x - 1] - S[y - 1][x - 1] + maze[y - 1][x - 1]

# クエリ処理
N = int(input())
for _ in range(N):
    A, B, C, D = map(int, input().split())
    total = S[C][D] - S[A - 1][D] - S[C][B - 1] + S[A - 1][B - 1]
    print(total)
