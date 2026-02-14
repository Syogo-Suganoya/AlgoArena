N = int(input())

SQUARE = dict([(c, int(c) ** 2) for c in "0123456789"])


def is_happy(n):
    s = set()
    while (n > 1) and (n not in s):
        s.add(n)
        n = sum(SQUARE[d] for d in str(n))
    return n == 1


print("Yes" if is_happy(N) else "No")
