S, T = input().split()
N = len(S)

# 幅 w を全探索（w = N のときは縦列が1文字になるだけで無意味）
for w in range(1, N):
    # 列のインデックスを動かす
    for c in range(w):
        tmp = []
        i = c
        # c 番目の列に相当する文字を、w 文字おきに取り出していく
        while i < N:
            tmp.append(S[i])
            i += w  # 次の行に対応する文字へジャンプ（縦に読む）

        # 集めた文字列が T と一致したら Yes
        if "".join(tmp) == T:
            print("Yes")
            exit()

# 最後まで一致する列がなければ No
print("No")
