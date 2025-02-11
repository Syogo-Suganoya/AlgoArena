N = int(input())
A = [list(input()) for _ in range(N)]


# グリッド A を出力する関数
def print_all(A):
    for i in range(N):
        for j in range(N):
            print(A[i][j], end="")
        print()


# 新しいグリッドを作成（空のグリッド）
new_A = [["" for _ in range(N)] for _ in range(N)]

# 各マスに対して、回転後の位置を計算し新しいグリッドに配置する
for y in range(N):
    for x in range(N):
        # (x, y) の位置が属する「層」を決定
        # 層は最小値で計算。どれだけ外周から離れているかを決める。
        d = min(
            x + 1, y + 1, N - x, N - y
        )  # 現在位置が属する層のサイズ（最外周からどれだけ離れているか）

        # 現在位置 (x, y) の回転後の位置 (nx, ny) を決める
        nx = x  # x座標を初期化
        ny = y  # y座標を初期化

        # 回転回数は d % 4 で決まる
        # 4回回ると元に戻るため、余りを使って回転回数を決定
        for i in range(d % 4):
            # 90度反時計回りの回転を行う
            # 反時計回りに90度回すために座標変換
            ty = nx  # 新しい y座標は元の x座標
            tx = N - 1 - ny  # 新しい x座標は、元の y座標から逆転した値
            nx = tx  # 新しい x座標
            ny = ty  # 新しい y座標

        # 回転後の位置 (nx, ny) に現在の値 A[y][x] を配置
        new_A[ny][nx] = A[y][x]

# 回転後の新しいグリッド new_A を出力
print_all(new_A)
