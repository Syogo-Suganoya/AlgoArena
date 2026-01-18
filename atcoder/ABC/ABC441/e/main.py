N = int(input())
S = input()

# A:+1, B:-1, C:0
P = [0]
for ch in S:
    if ch == "A":
        P.append(P[-1] + 1)
    elif ch == "B":
        P.append(P[-1] - 1)
    else:
        P.append(P[-1])

# 座標圧縮
vals = sorted(set(P))
idx = {v: i for i, v in enumerate(vals)}

# Fenwick Tree
fenwick = [0] * (len(vals) + 1)


def add(i, v):
    i += 1
    while i < len(fenwick):
        fenwick[i] += v
        i += i & -i


def sum_(i):
    i += 1
    s = 0
    while i > 0:
        s += fenwick[i]
        i -= i & -i
    return s


ans = 0

for x in P:
    i = idx[x]
    # x より小さい値の個数
    ans += sum_(i - 1)
    add(i, 1)

print(ans)
