MOD = 998244353


def modinv(x, m=MOD):
    """
    モジュラ逆元 (フェルマーの小定理)
    pow(x, m - 2, m) は (x^(m-2)) % m を計算する
    """
    return pow(x, m - 2, m)


n = int(input())

a = []  # a[i] = サイコロi の [面1, ..., 面6]
s_set = set()  # s_set = 存在する全ての目の値（ユニーク）

for _ in range(n):
    row = list(map(int, input().split()))
    a.append(row)
    for val in row:
        s_set.add(val)

# --- 座標圧縮 ---
# s = ユニークな目の値をソートしたもの
s = sorted(list(s_set))
k = len(s)  # ユニークな値の個数

# s_map = {値: sのインデックス} の辞書
s_map = {val: i for i, val in enumerate(s)}

# --- 前処理 ---
# upd[i] = 値 s[i] を持つサイコロのインデックス(j) のリスト
upd = [[] for _ in range(k)]
for i in range(n):
    for j in range(6):
        val = a[i][j]
        # 値からsのインデックスを高速に引く
        idx = s_map[val]
        upd[idx].append(i)

# --- 期待値の計算 ---
# E[X] = s[k-1] - sum( P(X <= s[i]) * (s[i+1] - s[i]) )
# C++コードは ans = s[k-1] + (-sum_term) / (6^N) を計算している

ans = 0
# b[j] = サイコロj の s[i] 以下の面の数
b = [0] * n
# prod = b[0] * b[1] * ... * b[n-1]
prod = 1
# zero_cnt = b[j] == 0 となっているサイコロjの数
zero_cnt = n

# s[0] から s[k-2] までループ
for i in range(k - 1):
    # i番目の値 s[i] を持つサイコロ j について b[j] を更新
    for j in upd[i]:
        if b[j] == 0:
            # このサイコロjが初めて 0 ではなくなる
            zero_cnt -= 1
        else:
            # prod から古い b[j] の寄与を除く (割り算)
            prod = (prod * modinv(b[j])) % MOD

        # b[j] をインクリメント
        b[j] += 1
        # prod に新しい b[j] の寄与を加える (掛け算)
        prod = (prod * b[j]) % MOD

    # この時点で、b[j] は s[i] 以下の面の数
    # prod は product(b)

    term = 0
    if zero_cnt == 0:
        # b[j] が全て 0 でない場合のみ
        # P(X <= s[i]) が 0 でない
        # term = product(b[j])
        term = prod

    # P(X <= s[i]) * (s[i+1] - s[i]) の (6^N) を除く部分を計算
    # ans -= (term * (s[i+1] - s[i]))
    delta_s = s[i + 1] - s[i]  # % MOD は不要
    ans = (ans - (term * delta_s) % MOD + MOD) % MOD

# ans は -sum( product(b) * (s[i+1]-s[i]) )

# 最後に 6^N で割る (6^N のモジュラ逆元を掛ける)
total_outcomes_inv = modinv(pow(6, n, MOD))
ans = (ans * total_outcomes_inv) % MOD

# s[k-1] を足す
ans = (ans + s[k - 1]) % MOD

print(ans)
