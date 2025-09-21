MOD = 10**9 + 7

S = input().strip()

ans = 0

# 左側の A の数、? の数
la, lp = 0, 0
# 右側の C の数、? の数
rc, rp = 0, 0

# まず右全体の C と ? を数える
for c in S:
    if c == "C":
        rc += 1
    if c == "?":
        rp += 1

for c in S:
    # 今の位置を使う前に右側のカウントを減らす
    if c == "C":
        rc -= 1
    if c == "?":
        rp -= 1

    if c == "?" or c == "B":
        # 左側の寄与
        l = (la * pow(3, lp, MOD) + lp * pow(3, lp - 1, MOD)) % MOD
        # 右側の寄与
        r = (rc * pow(3, rp, MOD) + rp * pow(3, rp - 1, MOD)) % MOD
        ans = (ans + l * r) % MOD

    # この文字を左側に移す
    if c == "A":
        la += 1
    if c == "?":
        lp += 1

print(ans % MOD)
