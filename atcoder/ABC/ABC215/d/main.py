N, M = map(int, input().split())
A = list(map(int, input().split()))

bad = set()

# A に含まれるすべての素因数を列挙
for a in A:
    tmp = a
    for p in range(2, int(tmp**0.5) + 1):
        if tmp % p == 0:
            bad.add(p)
            while tmp % p == 0:
                tmp //= p
    if tmp > 1:
        bad.add(tmp)

ok = [True] * (M + 1)

# bad に含まれる素因数の倍数を除外
for p in bad:
    for j in range(p, M + 1, p):
        ok[j] = False

# 答えの収集と出力
res = [i for i in range(1, M + 1) if ok[i]]
print(len(res))
for x in res:
    print(x)
