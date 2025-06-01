from collections import Counter

S = input()
T = input()

# 文字のカウント
cs = Counter(S)
ct = Counter(T)

# 文字種の差分計算
diff_s = {}
diff_t = {}

for c in "abcdefghijklmnopqrstuvwxyz":
    ds = cs[c] - ct[c]
    if ds > 0:
        diff_s[c] = ds
    elif ds < 0:
        diff_t[c] = -ds

# @ で補える文字
can_replace = set("atcoder")

# S側の@でTの差分を埋める
at_s = cs["@"]
for c, v in diff_t.items():
    if c in can_replace:
        at_s -= v
    else:
        # 補えない文字
        print("No")
        exit()

# T側の@でSの差分を埋める
at_t = ct["@"]
for c, v in diff_s.items():
    if c in can_replace:
        at_t -= v
    else:
        print("No")
        exit()

# @ の残数がマイナスなら補えない
print("Yes" if at_s >= 0 and at_t >= 0 else "No")
