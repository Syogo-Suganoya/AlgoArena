MOD = 10**9 + 7

s = int(input())
a = [0] * (s + 1)
a[0] = 1  # 和0の作り方は1通り（空集合）
# a[1], a[2]は初期化済みで0

for i in range(3, s + 1):
    a[i] = (a[i - 1] + a[i - 3]) % MOD

print(a[s])
