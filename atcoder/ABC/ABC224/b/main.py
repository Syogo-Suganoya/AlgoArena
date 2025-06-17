H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]


def main():
    for i1 in range(H):
        for i2 in range(i1 + 1, H):  # i1 < i2
            for j1 in range(W):
                for j2 in range(j1 + 1, W):  # j1 < j2
                    # チェック条件
                    if A[i1][j1] + A[i2][j2] > A[i1][j2] + A[i2][j1]:
                        return False
    return True


print("Yes" if main() else "No")
