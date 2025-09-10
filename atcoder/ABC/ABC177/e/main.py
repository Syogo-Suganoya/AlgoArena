import math

N = int(input())
A = list(map(int, input().split()))

MAX_A = 10**6

# ---------- Step1: 最小素因数 (SPF: smallest prime factor) を前計算 ----------
# エラトステネスで各数の最小素因数を持つ配列を作る
spf = [0] * (MAX_A + 1)
for i in range(2, MAX_A + 1):
    if spf[i] == 0:  # 素数
        for j in range(i, MAX_A + 1, i):
            if spf[j] == 0:
                spf[j] = i

# ---------- Step2: pairwise coprime 判定 ----------
# 各素数が何回出現したかを記録
seen = [False] * (MAX_A + 1)
pairwise = True
for x in A:
    factors = set()
    while x > 1:
        p = spf[x]
        factors.add(p)
        while x % p == 0:
            x //= p
    # 出現済みの素因数が再度現れたら pairwise 失敗
    for p in factors:
        if seen[p]:
            pairwise = False
            break
        seen[p] = True
    if not pairwise:
        break

if pairwise:
    print("pairwise coprime")
else:
    # ---------- Step3: setwise / not coprime 判定 ----------
    g = A[0]
    for x in A[1:]:
        g = math.gcd(g, x)
    if g == 1:
        print("setwise coprime")
    else:
        print("not coprime")
