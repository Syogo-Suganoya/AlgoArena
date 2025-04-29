def main():
    _, M = map(int, input().split())
    res = 0
    s = set()

    for _ in range(M):
        u, v = map(int, input().split())

        # 自己ループか
        if u == v:
            res += 1
            continue

        # 正規化
        if u > v:
            u, v = v, u

        # 多重ループか
        if (u, v) in s:
            res += 1
        else:
            s.add((u, v))

    print(res)


if __name__ == "__main__":
    main()
