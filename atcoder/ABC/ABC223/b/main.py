S = input()

mins = S
maxs = S

# Sの長さだけ回転して調べる
for _ in range(len(S) - 1):
    # 右シフト（実際は左シフトを使う方が書きやすい）
    S = S[1:] + S[0]

    # 最小・最大の更新
    mins = min(mins, S)
    maxs = max(maxs, S)

print(mins)
print(maxs)
