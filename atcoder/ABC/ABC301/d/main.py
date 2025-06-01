S = list(input())
N = int(input())

# すべての'?'を'0'に置き換えた場合の値を計算
min_val = int("".join(["0" if c == "?" else c for c in S]), 2)
if min_val > N:
    print(-1)
    exit()

# 上位ビットから順に処理
for i in range(len(S)):
    if S[i] == "?":
        S[i] = "1"
        temp = "".join(["0" if c == "?" else c for c in S])
        if int(temp, 2) <= N:
            continue
        else:
            S[i] = "0"

# 残りの'?'を'0'に置き換えた最終的な値を出力
result = "".join(["0" if c == "?" else c for c in S])
print(int(result, 2))
