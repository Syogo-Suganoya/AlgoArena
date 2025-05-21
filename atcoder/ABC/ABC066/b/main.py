S = input()

for i in range(1, len(S)):
    s = S[:-i]  # 末尾から i 文字削除
    if len(s) % 2 != 0:
        continue  # 偶数長でないならスキップ

    half = len(s) // 2
    if s[:half] == s[half:]:
        print(len(s))
        break
