A, B = map(int, input().split())


def main():
    if len({A, B}) == 1:
        return -1
    l = [1, 2, 3]
    l.remove(A)
    l.remove(B)
    return l[0]


print(main())
