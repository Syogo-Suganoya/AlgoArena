def main():
    N = int(input())
    A = [list(input()) for _ in range(N)]
    B = [list(input()) for _ in range(N)]

    for i in range(N):
        if A[i] == B[i]:
            continue
        for j in range(N):
            if A[i][j] != B[i][j]:
                print(i + 1, j + 1)
                return


main()
