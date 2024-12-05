def main():
    n, m = map(int, input().split())
    ans = []

    def dfs(v):
        sz = len(v)
        if sz == n:
            ans.append(v)
            return
        start = 1 if sz == 0 else v[-1] + 10
        end = m - 10 * (n - sz - 1) + 1
        for i in range(start, end):
            dfs(v + [i])

    dfs([])
    X = len(ans)
    print(X)
    for row in ans:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    main()
