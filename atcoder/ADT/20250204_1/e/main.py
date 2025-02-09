N, M = map(int, input().split())


def main():
    B = []
    for i in range(N):
        b = list(map(int, input().split()))
        B.append(b)
        if i == 0:
            if (B[0][0] - 1) % 7 + M > 7:
                return False
        for j in range(M):
            if i > 0:
                if B[i][j] - B[i - 1][j] != 7:
                    return False
            if j > 0:
                if B[i][j] - B[i][j - 1] != 1:
                    return False
    return True


print("Yes" if main() else "No")
