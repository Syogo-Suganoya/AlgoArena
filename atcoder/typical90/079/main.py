H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]


def main():
    directions = [(0, 0), (1, 0), (0, 1), (1, 1)]

    res = 0
    for i in range(H - 1):
        for j in range(W - 1):
            diff = B[i][j] - A[i][j]
            for dx, dy in directions:
                A[i + dx][j + dy] += diff
            res += abs(diff)
            if A == B:
                print("Yes")
                print(res)
                return

    print("No")


main()
