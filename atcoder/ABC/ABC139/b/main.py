A, B = map(int, input().split())


def main():
    c = 1
    res = 0
    while c < B:
        res += 1
        c += A
        c -= 1
    return res


print(main())
