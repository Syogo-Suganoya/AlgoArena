from collections import Counter

S = input().strip()
n = len(S)

# 右側での文字出現回数を初期化（全長分）
rcnt = Counter(S)
lcnt = Counter()  # 左側は空からスタート

ans = 0
for j in range(n):
    rcnt[S[j]] -= 1  # j を境界として右側から除外

    # この j を中間文字にする全回文は total over c of (lcnt[c] * rcnt[c])
    for c in lcnt:
        ans += lcnt[c] * rcnt[c]

    # 移動したら j を左側に含める
    lcnt[S[j]] += 1

print(ans)
