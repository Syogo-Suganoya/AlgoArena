def solve():
    n = int(input())
    s = input().strip()

    # c[i] は s[0..i-1] の 0 を +1, 1 を -1 とした累積和
    c = [0] * (n + 1)
    for i in range(n):
        if s[i] == "0":
            c[i + 1] = c[i] + 1
        else:
            c[i + 1] = c[i] - 1

    # 元の文字列中の '1' の総数
    sum_ones = s.count("1")

    ma = 0  # これまでの c[i] の最大値
    res = 0  # 最小値の更新に使う

    for i in range(n + 1):
        # res = min(これまでの res, c[i] - ma)
        res = min(res, c[i] - ma)
        ma = max(ma, c[i])

    # 答え = 元の '1' の数 + res
    # res は負の値なので、1 を最大化する効果になる
    print(sum_ones + res)


# 複数テストケースに対応
t = int(input())
for _ in range(t):
    solve()
