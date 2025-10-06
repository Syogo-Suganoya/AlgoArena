import sys

sys.setrecursionlimit(10**7)


def shortest_palindrome_with_prefix(S):
    # S の最短回文を、S を接頭辞として持つように作る

    n = len(S)
    T = S[::-1]  # 逆順にした文字列

    # KMP の next (失敗関数) を T + "#" + S に対して作る
    # こうすると、T の接頭辞 と S の接尾辞（逆順） のマッチの長さを調べられる
    U = T + "#" + S
    m = len(U)
    nxt = [0] * (m + 1)
    # nxt[i] = 長さ i の前半部分の最長の真の接尾辞接頭辞の長さ

    # 構築
    j = 0
    for i in range(1, m):
        while j > 0 and U[j] != U[i]:
            j = nxt[j]
        if U[j] == U[i]:
            j += 1
        nxt[i + 1] = j

    # nxt[m] が、T と S のマッチする最長の長さ
    L = nxt[m]
    # つまり、S の末尾から長さ L の接尾辞は、T の先頭から L 文字と一致する（逆順マッチしている）
    # だから S の前半部分（長さ n - L）を逆順に付け足せばよい
    add = S[: n - L][::-1]
    return S + add


S = input().strip()
ans = shortest_palindrome_with_prefix(S)
print(ans)
