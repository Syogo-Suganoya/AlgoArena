# 入力の読み込み
N = int(input())
A = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]

# 配列Aの読み込み
for x in range(1, N + 1):
    for y in range(1, N + 1):
        values = list(map(int, input().split()))
        for z in range(1, N + 1):
            A[x][y][z] = values[z - 1]

# 3D累積和の構築
S = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
for x in range(1, N + 1):
    for y in range(1, N + 1):
        for z in range(1, N + 1):
            S[x][y][z] = (
                A[x][y][z]
                + S[x - 1][y][z]
                + S[x][y - 1][z]
                + S[x][y][z - 1]
                - S[x - 1][y - 1][z]
                - S[x - 1][y][z - 1]
                - S[x][y - 1][z - 1]
                + S[x - 1][y - 1][z - 1]
            )

# クエリの処理
Q = int(input())
for _ in range(Q):
    Lx, Rx, Ly, Ry, Lz, Rz = map(int, input().split())
    # 累積和を用いて直方体領域の合計値を計算
    total = (
        S[Rx][Ry][Rz]
        - S[Lx - 1][Ry][Rz]
        - S[Rx][Ly - 1][Rz]
        - S[Rx][Ry][Lz - 1]
        + S[Lx - 1][Ly - 1][Rz]
        + S[Lx - 1][Ry][Lz - 1]
        + S[Rx][Ly - 1][Lz - 1]
        - S[Lx - 1][Ly - 1][Lz - 1]
    )
    print(total)
