S = input()
T = input()

# そのまま一致している場合はTrue
if S == T:
    print("Yes")
    exit()

# Sの長さを取得（SとTの長さは等しい前提）
N = len(S)

# 1文字目から隣接スワップを試す
for i in range(1, N):
    tmp = list(S)  # 文字列はイミュータブルなのでリストに変換
    # i-1 と i をスワップ
    tmp[i], tmp[i - 1] = tmp[i - 1], tmp[i]
    if "".join(tmp) == T:
        print("Yes")
        exit()

# どのスワップでも一致しない場合
print("No")
