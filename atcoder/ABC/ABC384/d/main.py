N, S = map(int, input().split())
A = list(map(int, input().split()))


def main():
    s = S % sum(A)
    cumsum = [0] * (N * 2 + 1)
    for i, num in enumerate(A * 2):
        cumsum[i + 1] = cumsum[i] + num
    cumsum = set(cumsum)

    for i in cumsum:
        if i + s in cumsum:
            print("Yes")
            return
    print("No")


main()
