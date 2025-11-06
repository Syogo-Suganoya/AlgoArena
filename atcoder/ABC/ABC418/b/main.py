S = input()
N = len(S)
ans = 0.0  # 最終的な最大値

c = "t"

for i in range(N):
    for j in range(i + 2, N):  # 長さが3以上必要
        if S[i] != "t" or S[j] != "t":
            continue  # 先頭と末尾が違うならスキップ

        sub = S[i : j + 1]
        x = sub.count(c)  # 部分文字列中の c の出現回数
        length = len(sub)

        # 填まり率を計算
        rate = (x - 2) / (length - 2)
        ans = max(ans, rate)

print(ans)
