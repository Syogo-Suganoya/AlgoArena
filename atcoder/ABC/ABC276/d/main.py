def factor_23(x):
    """x を 2 と 3 の因数で割り切れるだけ割り、
    (2を何回割れたか, 3を何回割れたか, 残った数) を返す"""
    p = q = 0

    # 2 で割れるだけ割る
    while x % 2 == 0:
        x //= 2
        p += 1

    # 3 で割れるだけ割る
    while x % 3 == 0:
        x //= 3
        q += 1

    return p, q, x


N = int(input())
A = list(map(int, input().split()))

# まず全ての a_i を (2^p, 3^q, m) に分解
facts = [factor_23(a) for a in A]

# m 部分（2でも3でも割れない部分）が全て同じか確認
m_first = facts[0][2]
for p, q, m in facts:
    if m != m_first:
        print(-1)
        exit()

# m が全て同じなら、2 と 3 の指数　p, q を最小に揃える
# p_min, q_min に揃えるのが最適
p_min = min(f[0] for f in facts)
q_min = min(f[1] for f in facts)

# 操作回数 = 全部を p_min, q_min にするために必要な合計
ans = 0
for p, q, m in facts:
    ans += (p - p_min) + (q - q_min)

print(ans)
