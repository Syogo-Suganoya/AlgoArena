def main():
    _ = int(input())
    P = list(map(int, input().split()))

    if max(P) == P[0]:
        if P.count(max(P)) >= 2:
            return 1
        return 0
    return max(P) - P[0] + 1


print(main())
