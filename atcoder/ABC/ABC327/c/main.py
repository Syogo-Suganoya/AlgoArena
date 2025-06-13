A = [list(map(int, input().split())) for _ in range(9)]


def main():
    # 各行のチェック
    for row in A:
        if len(set(row)) != 9:
            return False

    # 各列のチェック
    for col in zip(*A):
        if len(set(col)) != 9:
            return False

    # 各3×3マスのチェック
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            block = []
            for x in range(3):
                for y in range(3):
                    block.append(A[i + x][j + y])
            if len(set(block)) != 9:
                return False
    return True


print("Yes" if main() else "No")
