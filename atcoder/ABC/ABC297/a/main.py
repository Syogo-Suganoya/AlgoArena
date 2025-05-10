N, D = map(int, input().split())
T = list(map(int, input().split()))


def main():
    for i in range(1, N):
        if T[i] - T[i - 1] <= D:
            return T[i]
    return -1


print(main())
