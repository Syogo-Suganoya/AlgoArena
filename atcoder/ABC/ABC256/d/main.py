from itertools import groupby

N = int(input())

# 最大範囲は 10^6 程度で十分（問題によっては調整してね）
imos = [0] * (10**6 + 2)

# 差分配列の構築
for _ in range(N):
    L, R = map(int, input().split())
    imos[L] += 1
    imos[R] -= 1

# 累積和をとって重なり数を算出
for i in range(1, len(imos)):
    imos[i] += imos[i - 1]

# 1以上の箇所はすべて 1 に変換（バイナリ化）
imos = [1 if x > 0 else 0 for x in imos]

# ランレングス圧縮で区間検出
pos = 0
for key, group in groupby(imos):
    length = len(list(group))
    if key == 1:
        print(pos, pos + length)
    pos += length
