def main():
    S = list(input())
    T = list(input())

    stack = []
    res = []

    for i in range(len(S)):
        # 辞書順が後ろになるものは、スタック
        if S[i] < T[i]:
            stack.append(i)
            continue
        if S[i] == T[i]:
            continue
        S[i] = T[i]
        res.append("".join(S))

    # スタック消化
    while stack:
        i = stack.pop()
        S[i] = T[i]
        res.append("".join(S))

    print(len(res))
    print("\n".join(res))


def another():
    """
    https://atcoder.jp/contests/abc370/editorial/10894
    実装例 (O(N^2))

    まず S[i] > T[i] の位置を先頭から順に変更し、
    その後 S[i] < T[i] の位置を末尾から順に変更します。
    """
    s = list(input())
    t = list(input())
    ans = []
    v = []
    n = len(s)

    # s[i] > t[i] のインデックスを前から順に
    for i in range(n):
        if s[i] > t[i]:
            v.append(i)

    # s[i] < t[i] のインデックスを後ろから順に
    for i in reversed(range(n)):
        if s[i] < t[i]:
            v.append(i)

    sz = len(v)
    for i in range(sz):
        s[v[i]] = t[v[i]]  # s の対応位置を t に合わせる
        ans.append("".join(s))  # 文字列に戻して記録

    print(sz)
    for e in ans:
        print(e)


main()
