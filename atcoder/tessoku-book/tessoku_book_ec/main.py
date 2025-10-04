MOD = 10**9 + 7
BASE = 131  # 基数。文字コードとのぶつかりを避けるため大きめ


def build_hashes(s):
    n = len(s)
    h = [0] * (n + 1)  # h[i] は s[0:i]（1文字目〜i文字目）のハッシュ
    powB = [1] * (n + 1)  # powB[i] = BASE^i % MOD
    for i in range(1, n + 1):
        h[i] = (h[i - 1] * BASE + (ord(s[i - 1]) - ord("a") + 1)) % MOD
        powB[i] = (powB[i - 1] * BASE) % MOD
    return h, powB


def get_hash(h, powB, l, r):
    # 区間 [l, r]（1-indexed） のハッシュを返す
    # h[r] - h[l-1] * BASE^(r-l+1)
    res = h[r] - (h[l - 1] * powB[r - l + 1] % MOD)
    if res < 0:
        res += MOD
    return res


N, Q = map(int, input().split())
S = input().strip()

# 正順のハッシュ
h, powB = build_hashes(S)
# 逆順文字列
Srev = S[::-1]
# 逆順のハッシュ
hr, powBr = build_hashes(Srev)

for _ in range(Q):
    l, r = map(int, input().split())
    # 正順区間ハッシュ
    h1 = get_hash(h, powB, l, r)
    # 逆順対応区間のハッシュ：
    # 逆文字列上では位置換算が、元 S の [l,r] に対応するのは
    # Srev の区間 [N-r+1, N-l+1]
    rl = N - r + 1
    rr = N - l + 1
    h2 = get_hash(hr, powBr, rl, rr)
    if h1 == h2:
        print("Yes")
    else:
        print("No")
