N = int(input())

# Nのビットが立っている位置を取得
bits = []
for i in range(60):  # 60bitまで十分大きい
    if (N >> i) & 1:
        bits.append(i)

# 立っているビットの部分集合を列挙
res = []
for mask in range(1 << len(bits)):
    val = 0
    for j in range(len(bits)):
        if (mask >> j) & 1:
            val |= 1 << bits[j]
    res.append(val)

# 結果を昇順に出力
res.sort()
for v in res:
    print(v)
