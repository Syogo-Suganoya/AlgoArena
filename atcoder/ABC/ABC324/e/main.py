N, T = input().split()
N = int(N)
S = [input() for _ in range(N)]
M = len(T)


# 各文字列の prefix 長を求める
def prefix_len(s, t):
    """sの中でtのprefixをどこまで拾えるか"""
    j = 0
    for c in s:
        if j < len(t) and c == t[j]:
            j += 1
    return j


# 各文字列の suffix 長を求める
def suffix_len(s, t):
    """sの中でtのsuffixをどこまで拾えるか"""
    j = 0
    for c in reversed(s):
        if j < len(t) and c == t[-1 - j]:
            j += 1
    return j


prefixes = [prefix_len(s, T) for s in S]
suffixes = [suffix_len(s, T) for s in S]

# suffix 長の出現回数を集計
cnt = [0] * (M + 1)
for b in suffixes:
    cnt[b] += 1

# 後ろから累積和: cnt_ge[x] = suffix長 >= x の個数
cnt_ge = [0] * (M + 2)
cnt_ge[M] = cnt[M]
for i in range(M - 1, -1, -1):
    cnt_ge[i] = cnt_ge[i + 1] + cnt[i]

# ペアを数える
ans = 0
for a in prefixes:
    need = M - a  # 残り必要なsuffixの長さ
    ans += cnt_ge[need]

print(ans)
