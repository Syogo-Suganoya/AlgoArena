N = int(input())
S = input()
Q = int(input())

# 文字変換テーブル: a～zまでの初期値は自分自身
table = [chr(ord("a") + i) for i in range(26)]

for _ in range(Q):
    c, d = input().split()
    # 変換テーブルを書き換える
    for i in range(26):
        if table[i] == c:
            table[i] = d

# 変換後の文字列を構築
res = []
for ch in S:
    idx = ord(ch) - ord("a")
    res.append(table[idx])

print("".join(res))
