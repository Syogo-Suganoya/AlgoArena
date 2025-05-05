def main():
    M, D = map(int, input().split())
    y, m, d = map(int, input().split())

    if d != D:
        return (y, m, d + 1)

    d = 1
    if m == M:
        m = 1
        y += 1
    else:
        m += 1

    return (y, m, d)


print(*main())
