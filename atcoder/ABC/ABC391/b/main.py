N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(M)]


def f(i, j):
    if i + M > N or j + M > N:
        return False
    for i2 in range(M):
        for j2 in range(M):
            if T[i2][j2] != S[i + i2][j + j2]:
                return False
    return True


def main():
    for i in range(N):
        for j in range(N):
            if f(i, j):
                return (i + 1, j + 1)


print(*main())
