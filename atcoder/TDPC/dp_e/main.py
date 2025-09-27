# 桁DP
# 桁和mod

MOD = 10**9 + 7


def solve(N, D):
    digits = list(map(int, N))  # N を桁ごとのリストに変換
    L = len(digits)

    # dp[pos][mod][tight]:
    # pos    : 今見ている桁位置 (0..L)
    # mod    : 現在の桁和 mod D
    # tight  : 0=すでにN未満が確定, 1=ここまでNと一致
    dp = [[[0] * 2 for _ in range(D)] for _ in range(L + 1)]
    dp[0][0][1] = 1  # まだ何も選んでいないとき: 桁和=0, Nと一致

    for pos in range(L):
        for mod in range(D):
            for tight in range(2):
                val = dp[pos][mod][tight]
                if val == 0:
                    continue
                limit = digits[pos] if tight else 9
                for d in range(limit + 1):
                    new_mod = (mod + d) % D
                    new_tight = tight and (d == limit)
                    dp[pos + 1][new_mod][new_tight] += val
                    dp[pos + 1][new_mod][new_tight] %= MOD

    # 最後に桁和 mod D == 0 を満たす数の総数
    ans = (dp[L][0][0] + dp[L][0][1] - 1) % MOD  # -1 は「0」を除外
    return ans


# ---------- 入力 ----------
D = int(input().strip())
N = input().strip()

# ---------- 出力 ----------
print(solve(N, D))
