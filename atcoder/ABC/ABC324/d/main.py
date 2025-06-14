N = int(input())
S = input().strip()
sorted_S = sorted(S)  # 入力文字列をソートしておく

ans = 0
i = 0
max_num = 10**N

# i^2 が N 桁に収まる限りループ
while (sq := i * i) < max_num:
    s_sq = str(sq).zfill(N)  # ゼロ埋めでN桁に合わせる
    if sorted(s_sq) == sorted_S:  # 並べ替えで比較
        ans += 1
    i += 1

print(ans)
