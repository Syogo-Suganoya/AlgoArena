from collections import defaultdict

S = input().strip()
N = len(S)

mod = 2019

# 各余りの出現回数をカウントする辞書
count = defaultdict(int)
count[0] = 1  # 部分文字列がそのまま2019で割り切れるケース用

ans = 0
cur = 0  # suffixの累積余り
power10 = 1  # 10^k の係数（mod 2019 で扱う）

# 文字列を右から左に処理
for ch in reversed(S):
    digit = int(ch)
    cur = (cur + digit * power10) % mod
    ans += count[cur]  # 同じ余りが出てきた分だけ区間が作れる
    count[cur] += 1
    power10 = (power10 * 10) % mod  # 10^k を更新

print(ans)
