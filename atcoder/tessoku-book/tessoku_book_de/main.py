K, N = map(int, input().split())
A = list(map(int, input().split()))

dp = [False] * (K + 1)  # dp[i] = 石がi個のとき先手必勝か

for stones in range(1, K + 1):
    for a in A:
        if stones - a >= 0 and not dp[stones - a]:
            dp[stones] = True
            break  # 勝ちが確定したら抜ける

print("First" if dp[K] else "Second")
