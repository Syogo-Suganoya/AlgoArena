S = input().strip()
T = ""

# 2文字ずつステップを進める
for i in range(0, len(S), 2):
    T += S[i + 1]  # 偶数番目（0始まり）が i+1
    T += S[i]  # 奇数番目（0始まり）が i

print(T)
