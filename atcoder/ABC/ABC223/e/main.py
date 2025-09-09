def solve2(X, Y, S, T):
    for _ in range(2):
        length = (S + X - 1) // X  # X 方向に必要な行数
        if length < Y and X * (Y - length) >= T:
            return True
        X, Y = Y, X  # 横と縦を入れ替えて再チェック
    return False


def solve3(X, Y, A, B, C):
    for _ in range(2):
        for _ in range(3):
            length = (A + X - 1) // X
            if length < Y and solve2(X, Y - length, B, C):
                return True
            # A, B, C の順番を入れ替えて再チェック
            A, B, C = B, C, A
        X, Y = Y, X  # X, Y の入れ替え
    return False


# 入力
X, Y, A, B, C = map(int, input().split())
print("Yes" if solve3(X, Y, A, B, C) else "No")
