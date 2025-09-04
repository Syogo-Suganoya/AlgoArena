def lcp(s, t):
    """文字列 s と t の最長共通接頭辞 (LCP) の長さを求める"""
    res = 0
    # 先頭から順に比較して、一致する限りカウント
    for x, y in zip(s, t):
        if x == y:
            res += 1
        else:
            break
    return res


N = int(input())
S = [input().strip() for _ in range(N)]

# (インデックス, 文字列) の形にして、辞書順ソート
indexed = [(i, s) for i, s in enumerate(S)]
indexed.sort(key=lambda x: x[1])

# 各文字列に対して、最長共通接頭辞の長さを記録する配列
ans = [0] * N

# ソート後の隣接する文字列同士で LCP を計算
for i in range(N - 1):
    idx1, s1 = indexed[i]
    idx2, s2 = indexed[i + 1]
    length = lcp(s1, s2)
    # 双方の答えを更新（最大値を保持）
    ans[idx1] = max(ans[idx1], length)
    ans[idx2] = max(ans[idx2], length)

# 元の順序で出力
print(*ans, sep="\n")
