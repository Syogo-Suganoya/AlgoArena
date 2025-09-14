from functools import lru_cache

N = int(input())

S = str(N)
L = len(S)

# dp[pos][tight][first][last]
# - pos: 現在の桁 (0..L)
# - tight: 0=もうN未満確定, 1=まだ一致中
# - first: 最初の非ゼロ桁 (0..9, -1=未定→10扱い)
# - last: 今の末尾桁 (0..9, -1=未定→10扱い)


@lru_cache(None)
def dfs(pos, tight, first, last):
    if pos == L:
        # 最後まで到達したら (first,last) が確定
        if first != 10 and last != 10:
            return {(first, last): 1}
        else:
            return {}
    res = {}
    limit = int(S[pos]) if tight else 9
    for d in range(0, limit + 1):
        ntight = tight and (d == limit)
        nfirst = first
        nlast = last
        if first == 10 and d != 0:
            nfirst = d  # 最初の非ゼロ桁を確定
        if first != 10 or d != 0:
            nlast = d  # 数字が確定しているなら末尾を更新
        sub = dfs(pos + 1, ntight, nfirst, nlast)
        for k, v in sub.items():
            res[k] = res.get(k, 0) + v
    return res


cnt = dfs(0, 1, 10, 10)

# ペア (f,l) と (l,f) を掛け算して答えを得る
ans = 0
for (f, l), c in cnt.items():
    ans += c * cnt.get((l, f), 0)
print(ans)


# 別解
def another():
    N = int(input())
    c = [[0] * 10 for _ in range(10)]

    for x in range(1, N + 1):
        s = str(x)
        i = int(s[0])
        j = int(s[-1])
        c[i][j] += 1

    res = 0
    for i in range(1, 10):
        for j in range(1, 10):
            res += c[i][j] * c[j][i]

    print(res)
