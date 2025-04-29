# 公式解説から引用
# https://atcoder.jp/contests/abc376/editorial/11192


def num_move(n, from_, to, ng):
    if from_ > to:
        from_, to = to, from_
    if from_ < ng < to:
        return n + from_ - to
    else:
        return to - from_


n, q = map(int, input().split())
l, r = 1, 2
ans = 0

for _ in range(q):
    h, t = input().split()
    t = int(t)
    if h == "L":
        ans += num_move(n, l, t, r)
        l = t
    else:
        ans += num_move(n, r, t, l)
        r = t

print(ans)
