MOD = 10**9 + 7

# 入力
N, P = map(int, input().split())
A = list(map(int, input().split()))

# 各 A[i] を MOD で割った余りにしておく
A = [a % MOD for a in A]

# 出現回数をカウント
from collections import Counter

cnt = Counter(A)

ans = 0
for a in A:
    if a == 0:
        # a == 0 の場合、a*x ≡ P となるには P==0 のみ
        if P == 0:
            ans += N - 1  # 自分以外のすべてと組める
        continue

    # 逆元を計算
    inv_a = pow(a, MOD - 2, MOD)
    need = (P * inv_a) % MOD  # aと組むべき相手の値

    ans += cnt[need]
    # 自分自身を数えないように調整
    if need == a and (a * a) % MOD == P:
        ans -= 1

# (i, j) と (j, i) を両方数えているので 2 で割る
ans //= 2

print(ans)
