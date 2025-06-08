N, S = map(int, input().split())
A = list(map(int, input().split()))

# dp[x] = x を作れるかどうか
dp = [False] * (S + 1)
dp[0] = True  # 0 は必ず作れる（何も選ばない）

for a in A:  # 各要素 a について
    for x in range(S, a - 1, -1):  # 大きい方から逆順に更新（多重使用を防ぐ）
        if dp[x - a]:
            dp[x] = True

print("Yes" if dp[S] else "No")
