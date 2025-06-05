S = input()
T = input()

# S, T の長さは同じ前提
N = len(S)

# 文字をアルファベット順で 0〜25 に変換（ord('a') = 97）
S_nums = [ord(c) - ord("a") for c in S]
T_nums = [ord(c) - ord("a") for c in T]

# 差分（最初の文字でずらし量を決定）
diff = (T_nums[0] - S_nums[0]) % 26

# すべての文字で差分が同じかチェック
for s, t in zip(S_nums, T_nums, strict=True):
    if (t - s) % 26 != diff:
        print("No")
        break
else:
    print("Yes")
