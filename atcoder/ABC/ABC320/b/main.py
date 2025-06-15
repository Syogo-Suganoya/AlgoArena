S = input()

res = 0
N = len(S)

for l in range(N):
    for r in range(l + 1, N + 1):
        substr = S[l:r]
        if substr == substr[::-1]:  # 回文チェック
            res = max(res, r - l)  # 長さの最大値を更新

print(res)
