import collections


def main():
    A = list(map(str, input().split()))

    c = collections.Counter(A)
    most = c.most_common()[0][1]

    if most == 4:
        return 2
    if most == 3:
        return 1
    if most == 2:
        if c.most_common()[1][1] == 2:
            return 2
        return 1
    return 0


print(main())
