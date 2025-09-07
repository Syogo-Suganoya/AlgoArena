MOD = 998244353

T = int(input())
for _ in range(T):
    N = int(input())
    S = input().strip()

    # 前半の長さ
    L = (N + 1) // 2

    # S の前半を辞書順の数に変換（26進数っぽく扱う）
    base = 0
    for i in range(L):
        base = (base * 26 + (ord(S[i]) - ord("A"))) % MOD

    # base は「前半を自由に決めた回文の数」
    ans = (base + 1) % MOD

    # 実際に回文を作って S と比較する
    prefix = S[:L]
    if N % 2 == 0:
        cand = prefix + prefix[::-1]
    else:
        cand = prefix + prefix[:-1][::-1]

    if cand > S:
        ans = (ans - 1) % MOD

    print(ans % MOD)
