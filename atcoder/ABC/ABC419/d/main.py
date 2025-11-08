N, M = map(int, input().split())
s = input()
t = input()

cum = [0] * (N + 1)

# M 回の操作を差分配列に反映
for _ in range(M):
    l, r = map(int, input().split())
    cum[l - 1] += 1
    cum[r] -= 1

# 累積和
for i in range(N):
    cum[i + 1] += cum[i]

# 各文字の最終結果を決定
ans = [s[i] if cum[i] % 2 == 0 else t[i] for i in range(N)]

print("".join(ans))
