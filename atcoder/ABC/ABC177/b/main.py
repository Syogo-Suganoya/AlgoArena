S = input()
T = input()

N = len(S)
M = len(T)
res = M + 1  # 差分の最小値を初期化（Mより大きくしておく）

# 開始位置 i を動かしながら、S[i:i+M] の部分文字列と比較
for i in range(N - M + 1):
    diff = 0
    for j in range(M):
        if S[i + j] != T[j]:
            diff += 1
    res = min(res, diff)

print(res)

"""
S = input()
T = input()

N=len(S)
M=len(T)
res=M+1

N-Mまでループ
Sを[i:M]取得
Tとの差分数を取得
最低値を更新

"""
