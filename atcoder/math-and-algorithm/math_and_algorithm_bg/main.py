MOD = 10**9 + 7  # 剰余を取るための定数（10億7）

N = int(input())
A = list(map(int, input().split()))

ans = 0  # 最終的な答え（最大値の合計）
power = 1  # 2^i を計算するための変数。最初は 2^0 = 1

# 各要素 A[i] について、その要素が最大値になる部分集合の数は 2^i 通り
for a in A:
    ans = (ans + a * power) % MOD  # A[i] が最大となるすべての部分集合での合計を加算
    power = (power * 2) % MOD  # 次の 2^i を更新（i を 1 ずつ増やしていく）

print(ans)  # 最終的な合計を出力
