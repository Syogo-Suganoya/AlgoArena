A, B = map(int, input().split())


def main():
    if A == B:
        return 1
    if abs(A - B) % 2 == 0:
        return 3
    return 2


print(main())
