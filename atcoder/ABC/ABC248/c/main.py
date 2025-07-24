MOD = 998244353


class ModInt:
    def __init__(self, value):
        self.value = value % MOD

    def __iadd__(self, other):
        if isinstance(other, ModInt):
            self.value = (self.value + other.value) % MOD
        else:
            self.value = (self.value + other) % MOD
        return self

    def __add__(self, other):
        return ModInt(
            self.value + (other.value if isinstance(other, ModInt) else other)
        )

    def __int__(self):
        return self.value

    def __repr__(self):
        return str(self.value)


# 入力
n, m, K = map(int, input().split())

# dp[i][j] := i回振って合計jにする方法数（mod 998244353）
dp = [[ModInt(0) for _ in range(K + 1)] for _ in range(n + 1)]
dp[0][0] = ModInt(1)

for i in range(n):
    for j in range(K):
        for k in range(1, m + 1):
            if j + k <= K:
                dp[i + 1][j + k] += dp[i][j]

# 結果を合計
res = ModInt(0)
for i in range(1, K + 1):
    res += dp[n][i]

print(int(res))
