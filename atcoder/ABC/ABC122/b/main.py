S = input()
N = len(S)

l = 0  # 窓の左端
max_len = 0  # 結果保持

for r in range(N):  # rは窓の右端
    # 右端がACGT以外なら左端を右に移動
    if S[r] not in "ACGT":
        l = r + 1
    # 最大長を更新
    max_len = max(max_len, r - l + 1)

print(max_len)
