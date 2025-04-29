S = input()

res = 0

for i in range(len(S)):
    if S[i] != "A":
        continue  # Aでなければスキップ
    for j in range(i + 1, len(S)):
        if S[j] != "B":
            continue  # Bでなければスキップ
        distance = j - i  # AとBの間の文字数
        k = j + distance  # Bから右にdistance分進んだ場所
        if k < len(S) and S[k] == "C":
            res += 1  # Cならカウント増やす

print(res)
