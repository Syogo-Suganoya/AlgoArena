C = [list(map(int, input().split())) for _ in range(3)]


def main():
    # 1行目の横の差（行方向の増減）
    row_deltas = [C[0][1] - C[0][0], C[0][2] - C[0][1]]

    # 1列目の縦の差（列方向の増減）
    col_deltas = [C[1][0] - C[0][0], C[2][0] - C[1][0]]

    # ------------------------
    # 各行をチェック（行方向に正しく増減してるか）
    for i in range(3):
        for j in range(1, 3):
            expected = C[i][j - 1] + row_deltas[j - 1]
            if C[i][j] != expected:
                return False

    # ------------------------
    # 各列をチェック（列方向に正しく増減してるか）
    for j in range(3):
        for i in range(1, 3):
            expected = C[i - 1][j] + col_deltas[i - 1]
            if C[i][j] != expected:
                return False

    return True


print("Yes" if main() else "No")
